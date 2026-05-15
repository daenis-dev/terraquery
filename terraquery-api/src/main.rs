use axum::{
    extract::{Path, State},
    http::{HeaderValue, Method},
    response::IntoResponse,
    routing::{get, post},
    Json, Router,
};
use serde::{Deserialize, Serialize};
use std::{
    path::PathBuf,
    process::Command,
    sync::Arc,
};
use tower_http::cors::CorsLayer;

#[derive(Debug, serde::Deserialize)]
struct DemoSpecRenderRequest {
    spec: AnalysisSpec,
}

#[derive(Debug, Serialize)]
struct GenerateSpecRequest {
    query: String,
}

#[derive(Debug, Deserialize)]
struct GenerateSpecResponse {
    success: bool,
    spec: Option<AnalysisSpec>,
    raw_output: Option<String>,
    error: Option<String>,
}

#[derive(Debug, serde::Deserialize)]
struct DemoQueryRequest {
    query: String,
}

#[derive(Clone)]
struct AppState {
    data_root: PathBuf,
    potree_converter: PathBuf,
    potree_converter_dir: PathBuf,
    spec_generator_url: String,
}

#[derive(Debug, Serialize, Deserialize, Clone)]
struct AnalysisSpec {
    intent: String,
    target: String,
    conditions: AnalysisConditions,
    filters: AnalysisFilters,
    ranking: AnalysisRanking,
    render: AnalysisRender,
}

#[derive(Debug, Serialize, Deserialize, Clone)]
struct AnalysisConditions {
    proximity: ProximityCondition,
}

#[derive(Debug, Serialize, Deserialize, Clone)]
struct ProximityCondition {
    object: String,
    distance_meters: f64,
}

#[derive(Debug, Serialize, Deserialize, Clone)]
struct AnalysisFilters {
    min_height_meters: Option<f64>,
    min_cluster_size: Option<u64>,
}

#[derive(Debug, Serialize, Deserialize, Clone)]
struct AnalysisRanking {
    #[serde(rename = "type")]
    ranking_type: Option<String>,
    top_n: Option<u64>,
}

#[derive(Debug, Serialize, Deserialize, Clone)]
struct AnalysisRender {
    mode: String,
    show: Vec<String>,
}

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let spec_generator_url = std::env::var("SPEC_GENERATOR_URL")
        .unwrap_or_else(|_| "http://host.docker.internal:8000/generate-spec".to_string());

    let state = Arc::new(AppState {
        data_root: PathBuf::from("/data"),
        potree_converter: PathBuf::from(
            "/opt/potreeconverter/PotreeConverter_linux_x64/PotreeConverter",
        ),
        potree_converter_dir: PathBuf::from(
            "/opt/potreeconverter/PotreeConverter_linux_x64",
        ),
        spec_generator_url,
    });

    let cors = CorsLayer::new()
        .allow_origin("http://localhost:4200".parse::<HeaderValue>()?)
        .allow_methods([Method::GET, Method::POST, Method::OPTIONS])
        .allow_headers(tower_http::cors::Any);

    let app = Router::new()
        .route("/health", get(health))
        .route("/api/demo-tiles/:tile_id/render", post(render_demo_tile))
        .route(
            "/api/demo-tiles/:tile_id/query",
            post(render_demo_from_natural_language_query),
        )
        .route(
            "/api/demo-tiles/:tile_id/render-spec",
            post(render_demo_from_spec),
        )
        .layer(cors)
        .with_state(state);

    let listener = tokio::net::TcpListener::bind("0.0.0.0:8080").await?;

    println!("TerraQuery API running at http://localhost:8080");

    axum::serve(listener, app).await?;

    Ok(())
}

async fn health() -> impl IntoResponse {
    Json(serde_json::json!({ "status": "ok" }))
}

async fn render_demo_tile(
    Path(tile_id): Path<String>,
    State(state): State<Arc<AppState>>,
) -> impl IntoResponse {
    if !is_valid_demo_tile_id(&tile_id) {
        return Json(serde_json::json!({
            "status": "error",
            "message": "Invalid demo tile id"
        }));
    }

    let source_path = state
        .data_root
        .join("demo-tiles")
        .join(format!("{tile_id}_cleaned.las"));

    if !source_path.exists() {
        return Json(serde_json::json!({
            "status": "error",
            "message": format!("Demo tile file not found: {}", source_path.display())
        }));
    }

    let output_dir = state
        .data_root
        .join("pointclouds")
        .join("demo")
        .join(&tile_id);

    let metadata_path = output_dir.join("metadata.json");
    let potree_url = demo_potree_url(&tile_id);

    if metadata_path.exists() {
        return Json(serde_json::json!({
            "status": "ready",
            "tile_id": tile_id,
            "potree_url": potree_url,
            "mode": "demo"
        }));
    }

    if let Err(err) = std::fs::create_dir_all(&output_dir) {
        return Json(serde_json::json!({
            "status": "error",
            "message": format!("Could not create demo output directory: {}", err)
        }));
    }

    let status = Command::new(&state.potree_converter)
        .arg(&source_path)
        .arg("-o")
        .arg(&output_dir)
        .env("LD_LIBRARY_PATH", &state.potree_converter_dir)
        .status();

    match status {
        Ok(exit_status) if exit_status.success() => Json(serde_json::json!({
            "status": "ready",
            "tile_id": tile_id,
            "potree_url": potree_url,
            "mode": "demo"
        })),
        Ok(exit_status) => Json(serde_json::json!({
            "status": "error",
            "message": format!("PotreeConverter failed: {}", exit_status)
        })),
        Err(err) => Json(serde_json::json!({
            "status": "error",
            "message": format!("Failed to run PotreeConverter: {}", err)
        })),
    }
}

async fn render_demo_from_natural_language_query(
    Path(tile_id): Path<String>,
    State(state): State<Arc<AppState>>,
    Json(request): Json<DemoQueryRequest>,
) -> impl IntoResponse {
    if !is_valid_demo_tile_id(&tile_id) {
        return Json(serde_json::json!({
            "status": "error",
            "message": "Invalid demo tile id"
        }));
    }

    if request.query.trim().is_empty() {
        return Json(serde_json::json!({
            "status": "error",
            "message": "Query is required"
        }));
    }

    let spec = match generate_spec_from_model(&state, request.query.trim()).await {
        Ok(spec) => spec,
        Err(err) => {
            return Json(serde_json::json!({
                "status": "error",
                "message": format!("Could not generate analysis spec: {}", err)
            }));
        }
    };

    render_demo_analysis_result(
        &state,
        &tile_id,
        &spec,
        serde_json::json!({
            "query": request.query,
            "mode": "query"
        }),
    )
}

async fn render_demo_from_spec(
    Path(tile_id): Path<String>,
    State(state): State<Arc<AppState>>,
    Json(request): Json<DemoSpecRenderRequest>,
) -> impl IntoResponse {
    if !is_valid_demo_tile_id(&tile_id) {
        return Json(serde_json::json!({
            "status": "error",
            "message": "Invalid demo tile id"
        }));
    }

    render_demo_analysis_result(
        &state,
        &tile_id,
        &request.spec,
        serde_json::json!({
            "mode": "manual-spec"
        }),
    )
}

fn render_demo_analysis_result(
    state: &AppState,
    tile_id: &str,
    spec: &AnalysisSpec,
    extra_response_fields: serde_json::Value,
) -> Json<serde_json::Value> {
    let render_id = format!(
        "{}-{}",
        spec_to_render_id(spec),
        unique_render_suffix()
    );

    let source_path = state
        .data_root
        .join("demo-tiles")
        .join(format!("{tile_id}_cleaned.las"));

    if !source_path.exists() {
        return Json(serde_json::json!({
            "status": "error",
            "message": format!("Demo tile file not found: {}", source_path.display())
        }));
    }

    let work_dir = state
        .data_root
        .join("demo-renders")
        .join(tile_id);

    let rendered_las_path = work_dir.join(format!("{render_id}.las"));

    let output_dir = state
        .data_root
        .join("pointclouds")
        .join("demo-renders")
        .join(tile_id)
        .join(&render_id);

    if let Err(err) = std::fs::create_dir_all(&work_dir) {
        return Json(serde_json::json!({
            "status": "error",
            "message": format!("Could not create demo render work directory: {}", err)
        }));
    }

    if let Err(err) = std::fs::create_dir_all(&output_dir) {
        return Json(serde_json::json!({
            "status": "error",
            "message": format!("Could not create demo render output directory: {}", err)
        }));
    }

    let spec_json = match serde_json::to_string(spec) {
        Ok(json) => json,
        Err(err) => {
            return Json(serde_json::json!({
                "status": "error",
                "message": format!("Could not serialize analysis spec: {}", err)
            }));
        }
    };

    let status = Command::new("python3")
        .arg("/app/scripts/render_demo_classes.py")
        .arg("--input")
        .arg(&source_path)
        .arg("--output")
        .arg(&rendered_las_path)
        .arg("--spec")
        .arg(spec_json)
        .status();

    match status {
        Ok(exit_status) if exit_status.success() => {}
        Ok(exit_status) => {
            return Json(serde_json::json!({
                "status": "error",
                "message": format!("Demo render script failed with status: {}", exit_status)
            }));
        }
        Err(err) => {
            return Json(serde_json::json!({
                "status": "error",
                "message": format!("Failed to run demo render script: {}", err)
            }));
        }
    }

    let status = Command::new(&state.potree_converter)
        .arg(&rendered_las_path)
        .arg("-o")
        .arg(&output_dir)
        .env("LD_LIBRARY_PATH", &state.potree_converter_dir)
        .status();

    match status {
        Ok(exit_status) if exit_status.success() => {
            let mut response = serde_json::json!({
                "status": "ready",
                "tile_id": tile_id,
                "applied_spec": spec,
                "potree_url": format!(
                    "http://localhost:4200/pointclouds/demo-renders/{}/{}/metadata.json",
                    tile_id,
                    render_id
                )
            });

            merge_json_object(&mut response, extra_response_fields);

            Json(response)
        }
        Ok(exit_status) => Json(serde_json::json!({
            "status": "error",
            "message": format!("PotreeConverter failed: {}", exit_status)
        })),
        Err(err) => Json(serde_json::json!({
            "status": "error",
            "message": format!("Failed to run PotreeConverter: {}", err)
        })),
    }
}

async fn generate_spec_from_model(
    state: &AppState,
    query: &str,
) -> anyhow::Result<AnalysisSpec> {
    let client = reqwest::Client::new();

    let response = client
        .post(&state.spec_generator_url)
        .json(&GenerateSpecRequest {
            query: query.to_string(),
        })
        .send()
        .await?;

    if !response.status().is_success() {
        anyhow::bail!("Spec generator returned HTTP {}", response.status());
    }

    let parsed: GenerateSpecResponse = response.json().await?;

    if !parsed.success {
        anyhow::bail!(
            "Spec generator failed. raw_output={:?}, error={:?}",
            parsed.raw_output,
            parsed.error
        );
    }

    parsed
        .spec
        .ok_or_else(|| anyhow::anyhow!("Spec generator returned success=true but no spec"))
}

fn spec_to_render_id(spec: &AnalysisSpec) -> String {
    let distance_label = format!("{:.2}", spec.conditions.proximity.distance_meters)
        .trim_end_matches('0')
        .trim_end_matches('.')
        .replace('.', "p");

    let show_label = if spec.render.show.is_empty() {
        "none".to_string()
    } else {
        spec.render.show.join("-")
    };

    let ranking_label = match (&spec.ranking.ranking_type, spec.ranking.top_n) {
        (Some(ranking_type), Some(top_n)) => format!("rank-{}-top{}", ranking_type, top_n),
        (Some(ranking_type), None) => format!("rank-{}", ranking_type),
        _ => "rank-none".to_string(),
    };

    let height_label = spec
        .filters
        .min_height_meters
        .map(|value| format!("h{}", format!("{:.1}", value).replace('.', "p")))
        .unwrap_or_else(|| "h-none".to_string());

    let cluster_label = spec
        .filters
        .min_cluster_size
        .map(|value| format!("cluster{}", value))
        .unwrap_or_else(|| "cluster-none".to_string());

    let raw = format!(
        "{}-target-{}-object-{}-{}m-mode-{}-show-{}-{}-{}-{}-v1",
        spec.intent,
        spec.target,
        spec.conditions.proximity.object,
        distance_label,
        spec.render.mode,
        show_label,
        ranking_label,
        height_label,
        cluster_label
    );

    sanitize_render_id(&raw)
}

fn unique_render_suffix() -> String {
    let now = std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .unwrap_or_default();

    format!("run-{}", now.as_millis())
}

fn sanitize_render_id(value: &str) -> String {
    value
        .chars()
        .map(|character| {
            if character.is_ascii_alphanumeric() || character == '-' || character == '_' {
                character
            } else {
                '-'
            }
        })
        .collect::<String>()
        .split('-')
        .filter(|part| !part.is_empty())
        .collect::<Vec<_>>()
        .join("-")
}

fn is_valid_demo_tile_id(tile_id: &str) -> bool {
    tile_id == "N031E314" || tile_id == "N200E044"
}

fn demo_potree_url(tile_id: &str) -> String {
    format!("http://localhost:4200/pointclouds/demo/{}/metadata.json", tile_id)
}

fn merge_json_object(target: &mut serde_json::Value, source: serde_json::Value) {
    let Some(target_object) = target.as_object_mut() else {
        return;
    };

    let Some(source_object) = source.as_object() else {
        return;
    };

    for (key, value) in source_object {
        target_object.insert(key.clone(), value.clone());
    }
}