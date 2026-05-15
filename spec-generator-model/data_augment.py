from __future__ import annotations

import argparse
import copy
import json
import math
import random
import re
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple

Entry = Dict[str, Any]

DEFAULT_DISTANCE_METERS = 2
CLUSTER_DEFAULT_DISTANCE_METERS = 2

DEFAULT_DISTANCES_METERS = [
    0.5, 1, 1, 1.5, 1.5,
    2, 2, 2, 2.5, 2.5,
    3, 3, 4, 4, 5, 5,
    6, 7, 7.5, 8, 9, 10,
    12, 15, 20, 25, 30
]

NUMBER_WORDS = {
    0.5: ["half a", "0.5"],
    1: ["one", "1"],
    1.5: ["one and a half", "1.5"],
    2: ["two", "2"],
    2.5: ["two and a half", "2.5"],
    3: ["three", "3"],
    4: ["four", "4"],
    5: ["five", "5"],
    6: ["six", "6"],
    7: ["seven", "7"],
    7.5: ["seven and a half", "7.5"],
    8: ["eight", "8"],
    9: ["nine", "9"],
    10: ["ten", "10"],
    12: ["twelve", "12"],
    15: ["fifteen", "15"],
    20: ["twenty", "20"],
    25: ["twenty five", "25"],
    30: ["thirty", "30"],
}

SINGULAR_METER_UNITS = ["meter", "metre", "m"]
PLURAL_METER_UNITS = ["meters", "metres", "m"]

VEGETATION_TERMS = [
    "vegetation", "trees", "tree canopy", "canopy", "brush",
    "foliage", "overgrowth", "plant growth", "greenery"
]

STRUCTURE_TERMS = [
    "structures", "buildings", "building footprints", "roofs", "rooflines"
]

ENCROACHMENT_TERMS = [
    "encroachment", "vegetation encroachment", "vegetation conflicts",
    "clearance issues", "proximity issues", "vegetation problems", "tree conflicts"
]

COMMAND_VERBS = ["Show", "Display", "Highlight", "Find", "Locate", "Identify", "Visualize", "Render", "Map"]
QUESTION_PREFIXES = ["Where is", "Where are", "Which areas have", "Which structures have", "Can you show", "Can you find"]

# Balanced for FLAN-T5 Small:
# - enough basic examples
# - enough non-default render/filter/ranking examples
# - ranking classes no longer underrepresented
CATEGORY_RATIOS = {
    "basic": 0.28,
    "render_vegetation_only": 0.08,
    "render_structures_only": 0.08,
    "render_encroachment_only": 0.07,
    "filter_height": 0.12,
    "filter_cluster": 0.12,
    "ranking_point_count": 0.10,
    "ranking_height": 0.07,
    "ranking_severity": 0.08,
}

BAD_PATTERNS = [
    "Which structures have structures",
    "Which structures have buildings",
    "Which structures have building footprints",
    "Which structures have roofs",
    "Which structures have rooflines",
    "trees conflicts",
    "vegetation growing growing",
    "canopy growing growing",
    "plant growth growing growing",
]

VAGUE_DISTANCE_PATTERNS = [
    r"\bnearby\b",
    r"\bnear\b",
    r"\baround\b",
    r"\bsurrounding\b",
    r"\bcontext\b",
    r"\btoo close\b",
    r"\bencroaching\b",
    r"\bencroachment\b",
    r"\bconflicts?\b",
    r"\baffected\b",
    r"\bimpacted\b",
    r"\bonly\b",
    r"\bproblematic\b",
    r"\bclearance\b",
    r"\bissues?\b",
    r"\bhazards?\b",
    r"\bproblems?\b",
    r"\bclosest\b",
    r"\bnearest\b",
    r"\bworst\b",
    r"\bsevere\b",
    r"\bcritical\b",
]

CLUSTER_DISTANCE_PATTERNS = [
    r"\bclusters?\b",
    r"\bpatches\b",
    r"\bisolated vegetation points\b",
    r"\bvegetation points\b",
    r"\bdense vegetation\b",
    r"\blargest vegetation clusters\b",
]

EXPLICIT_DISTANCE_PATTERN = re.compile(
    r"\b(?:"
    r"\d+(?:\.\d+)?|"
    r"half a|one|two|three|four|five|six|seven|eight|nine|ten|"
    r"twelve|fifteen|twenty|twenty five|thirty|"
    r"one and a half|two and a half|seven and a half"
    r")\s*(?:m|meter|meters|metre|metres|ft|feet|foot)\b(?!\s*tall)",
    re.IGNORECASE,
)

BASIC_TEMPLATES = [
    "{verb} {veg} within {distance_text} {unit} of {structure}",
    "{verb} all {veg} within {distance_text}{compact_unit} of {structure}",
    "{verb} {veg} growing within {distance_text} {unit} of {structure}",
    "{verb} {veg} encroaching on {structure} within {distance_text} {unit}",
    "{verb} {veg} near {structure} within {distance_text} {unit}",
    "{verb} {issue} within {distance_text} {unit} of {structure}",
    "{veg_question} {veg} within {distance_text} {unit} of {structure}?",
    "Show me where {veg} {growth_phrase} within {distance_text} {unit} of {structure}",
    "Find places where {veg} conflicts with {structure} within {distance_text} {unit}",
    "Locate areas where {veg} may be encroaching on {structure} within {distance_text} {unit}",
]

RENDER_VEGETATION_ONLY_TEMPLATES = [
    "Show only the vegetation encroaching on {structure}",
    "Show only the vegetation encroaching on {structure} within {distance_text} {unit}",
    "Highlight only the offending {veg}",
    "Highlight only the offending {veg} within {distance_text} {unit} of {structure}",
    "Display {veg} conflicts without showing {structure}",
    "Visualize only problematic {veg} near {structure}",
    "Visualize only problematic {veg} near {structure} within {distance_text} {unit}",
    "Show just the encroaching {veg}",
    "Render vegetation only",
    "Hide structures and show vegetation conflicts",
    "Display only nearby vegetation",
    "Show vegetation overlays only",
    "Visualize vegetation without structures",
    "Highlight vegetation regions only",
]

RENDER_STRUCTURES_ONLY_TEMPLATES = [
    "Show {structure} affected by {veg}",
    "Show {structure} affected by {veg} within {distance_text} {unit}",
    "Highlight impacted {structure} only",
    "Display {structure} with encroachment issues",
    "Visualize affected {structure}",
    "Show only the {structure} that {structure_have} nearby {veg}",
    "Show impacted structures only",
    "Hide vegetation and show affected roofs",
    "Display only affected buildings",
    "Visualize impacted structures without vegetation",
]

RENDER_ENCROACHMENT_ONLY_TEMPLATES = [
    "Show only encroachment zones",
    "Highlight {issue}",
    "Display only problematic areas",
    "Visualize vegetation conflict regions",
    "Show only the conflict areas",
    "Show only the conflict areas within {distance_text} {unit}",
]

FILTER_HEIGHT_TEMPLATES = [
    "Ignore low vegetation and show conflicts",
    "Ignore low vegetation and show conflicts within {distance_text} {unit}",
    "Only show vegetation taller than {height} meters near {structure}",
    "Filter out small brush around {structure}",
    "Show tall trees near {structure}",
    "Show tall trees near {structure} within {distance_text} {unit}",
    "Display encroachment from vegetation over {height} meters tall",
]

FILTER_CLUSTER_TEMPLATES = [
    "Ignore isolated vegetation points",
    "Ignore isolated vegetation points within {distance_text} {unit} of {structure}",
    "Only show large vegetation clusters near {structure}",
    "Filter out small patches around {structure}",
    "Show significant vegetation conflicts only",
    "Display clusters of at least {cluster_size} vegetation points",
]

RANKING_POINT_COUNT_TEMPLATES = [
    "Show the top {top_n} biggest vegetation clusters",
    "Find the {top_n} largest encroachment clusters",
    "Display the top {top_n} largest conflict areas",
    "Show the top {top_n} densest vegetation regions within {distance_text} {unit}",
    "Find the top {top_n} largest vegetation clusters near {structure}",
    "Show the top {top_n} largest vegetation regions",
    "Display the {top_n} biggest vegetation areas",
]

RANKING_HEIGHT_TEMPLATES = [
    "Show the top {top_n} tallest vegetation conflicts",
    "Find the {top_n} tallest trees encroaching on {structure}",
    "Display the tallest canopy conflicts",
    "Show vegetation conflicts ranked by height",
    "Show the top {top_n} tallest vegetation conflicts within {distance_text} {unit}",
    "Show the top {top_n} highest canopy conflicts",
    "Find the {top_n} highest vegetation hazards",
    "Show the {top_n} greatest vertical encroachments",
    "Display the top {top_n} tallest overgrowth conflicts",
]

RANKING_SEVERITY_TEMPLATES = [
    "Show the top {top_n} biggest threats",
    "Find the {top_n} most severe vegetation conflicts",
    "Highlight the top {top_n} highest risk encroachment areas",
    "Display the {top_n} worst vegetation hazards",
    "Show the top {top_n} critical canopy conflicts within {distance_text} {unit}",
    "Show the top {top_n} highest threat areas",
    "Find the {top_n} most dangerous vegetation conflicts",
    "Display the {top_n} worst clearance violations",
    "Show the {top_n} most severe encroachments",
]

CATEGORY_TEMPLATES = {
    "basic": BASIC_TEMPLATES,
    "render_vegetation_only": RENDER_VEGETATION_ONLY_TEMPLATES,
    "render_structures_only": RENDER_STRUCTURES_ONLY_TEMPLATES,
    "render_encroachment_only": RENDER_ENCROACHMENT_ONLY_TEMPLATES,
    "filter_height": FILTER_HEIGHT_TEMPLATES,
    "filter_cluster": FILTER_CLUSTER_TEMPLATES,
    "ranking_point_count": RANKING_POINT_COUNT_TEMPLATES,
    "ranking_height": RANKING_HEIGHT_TEMPLATES,
    "ranking_severity": RANKING_SEVERITY_TEMPLATES,
}

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Augment TerraQuery JSONL training data with balanced spec categories.")
    parser.add_argument("--input", default="dataset.jsonl")
    parser.add_argument("--output", default="dataset_augmented.jsonl")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--target-size", type=int, default=15000)
    parser.add_argument("--include-feet", action="store_true")
    parser.add_argument("--include-originals", action=argparse.BooleanOptionalAction, default=True)
    return parser.parse_args()


def load_jsonl(path: Path) -> List[Entry]:
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    entries: List[Entry] = []

    with path.open("r", encoding="utf-8") as f:
        for line_number, raw_line in enumerate(f, start=1):
            line = raw_line.strip()

            if not line:
                continue

            try:
                entry = json.loads(line)
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSON on line {line_number}: {exc}") from exc

            if "input" not in entry or "output" not in entry:
                raise ValueError(f"Line {line_number} must contain 'input' and 'output' keys")

            entries.append(normalize_seed_entry(entry))

    return entries


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.strip()).lower()


def distance_label(distance: float) -> str:
    return str(int(distance)) if float(distance).is_integer() else str(distance).rstrip("0").rstrip(".")


def distance_text_options(distance_meters: float) -> List[str]:
    options = NUMBER_WORDS.get(distance_meters, [distance_label(distance_meters)])
    return list(dict.fromkeys(options + [distance_label(distance_meters)]))


def is_singular_distance_phrase(distance_text: str) -> bool:
    return distance_text in {"half a", "one", "1", "0.5"}


def units_for_distance_text(distance_text: str) -> List[str]:
    return SINGULAR_METER_UNITS if is_singular_distance_phrase(distance_text) else PLURAL_METER_UNITS


def compact_unit(unit: str) -> str:
    return f" {unit}"


def verb_for_veg(term: str) -> str:
    return "are" if term == "trees" else "is"


def verb_for_structure(term: str) -> str:
    return "have"


def clean_query(query: str) -> str:
    query = re.sub(r"\s+", " ", query)
    query = query.replace(" ?", "?")
    query = query.replace(" .", ".")
    query = query.strip()

    replacements = {
        "half a meters": "half a meter",
        "half a metres": "half a metre",
        "one meters": "one meter",
        "one metres": "one metre",
        "1 meters": "1 meter",
        "1 metres": "1 metre",
        "0.5 meters": "0.5 meter",
        "0.5 metres": "0.5 metre",
        "trees is": "trees are",
        "infrastructure that have": "infrastructure that has",
        "infrastructure have": "infrastructure has",
        "utility infrastructure have": "utility infrastructure has",
        "all all": "all",
        "Where are vegetation": "Where is vegetation",
        "Where are canopy": "Where is canopy",
        "Where are tree canopy": "Where is tree canopy",
        "Where are brush": "Where is brush",
        "Where are foliage": "Where is foliage",
        "Where are overgrowth": "Where is overgrowth",
        "Where are plant growth": "Where is plant growth",
        "Where are greenery": "Where is greenery",
        "Where is trees": "Where are trees",
        "trees conflicts": "trees conflict",
        "trees conflicts with": "trees conflict with",
        "vegetation growing growing": "vegetation growing",
        "canopy growing growing": "canopy growing",
        "tree canopy growing growing": "tree canopy growing",
        "plant growth growing growing": "plant growth growing",
        "brush growing growing": "brush growing",
        "foliage growing growing": "foliage growing",
        "overgrowth growing growing": "overgrowth growing",
        "greenery growing growing": "greenery growing",
        "plant growth growing": "plant growth",
        "overgrowth growing": "overgrowth",
        "greenery growing": "greenery",
        "foliage growing": "foliage",
        "brush growing": "brush",
        "tree canopy growing": "tree canopy",
        "canopy growing": "canopy",
    }

    for bad, good in replacements.items():
        query = query.replace(bad, good)

    return query


def is_bad_query(query: str) -> bool:
    normalized = normalize_text(query)
    return any(normalize_text(pattern) in normalized for pattern in BAD_PATTERNS)


def has_explicit_distance(query: str) -> bool:
    for match in EXPLICIT_DISTANCE_PATTERN.finditer(query):
        trailing = query[match.end():match.end() + 16].lower()

        if re.match(r"\s*(tall|high|height)\b", trailing):
            continue

        return True

    return False


def is_vague_nearby_query(query: str) -> bool:
    normalized = normalize_text(query)
    return any(re.search(pattern, normalized) for pattern in VAGUE_DISTANCE_PATTERNS)

def is_cluster_query(query: str) -> bool:
    normalized = normalize_text(query)
    return any(re.search(pattern, normalized) for pattern in CLUSTER_DISTANCE_PATTERNS)


def question_prefix_for_subject(subject: str) -> str:
    normalized = normalize_text(subject)

    plural_subjects = {
        "trees",
        "structures",
        "buildings",
        "building footprints",
        "roofs",
        "rooflines",
        "vegetation conflicts",
        "clearance issues",
        "proximity issues",
        "vegetation problems",
        "tree conflicts",
    }

    if normalized in plural_subjects:
        return "Where are"

    return "Where is"


def normalize_spec_contract(spec: Dict[str, Any]) -> Dict[str, Any]:
    spec = copy.deepcopy(spec)
    spec.setdefault("intent", "encroachment_analysis")
    spec.setdefault("target", "structures")
    spec.setdefault("conditions", {}).setdefault("proximity", {})
    spec["conditions"]["proximity"].setdefault("object", "vegetation")
    spec["conditions"]["proximity"].setdefault("distance_meters", DEFAULT_DISTANCE_METERS)
    spec.setdefault("filters", {})
    spec["filters"].setdefault("min_height_meters", None)
    spec["filters"].setdefault("min_cluster_size", None)
    spec.setdefault("ranking", {})
    spec["ranking"].setdefault("type", None)
    spec["ranking"].setdefault("top_n", None)
    spec.setdefault("render", {})
    spec["render"].setdefault("mode", "highlight")
    spec["render"].setdefault("show", ["structures", "vegetation", "encroachment"])
    return spec


def enforce_query_distance_rule(query: str, spec: Dict[str, Any]) -> Dict[str, Any]:
    spec = normalize_spec_contract(spec)

    if has_explicit_distance(query):
        return spec

    if is_cluster_query(query):
        spec["conditions"]["proximity"]["distance_meters"] = CLUSTER_DEFAULT_DISTANCE_METERS
        return spec

    if is_vague_nearby_query(query):
        spec["conditions"]["proximity"]["distance_meters"] = DEFAULT_DISTANCE_METERS
        return spec

    spec["conditions"]["proximity"]["distance_meters"] = DEFAULT_DISTANCE_METERS
    return spec


def normalize_seed_entry(entry: Entry) -> Entry:
    cleaned_input = clean_query(entry["input"])
    spec = enforce_query_distance_rule(cleaned_input, entry["output"])
    return {"input": cleaned_input, "output": spec}


def set_distance_meters(spec: Dict[str, Any], distance_meters: float) -> Dict[str, Any]:
    cloned = normalize_spec_contract(spec)
    cloned["conditions"]["proximity"]["distance_meters"] = distance_meters
    return cloned


def basic_spec_from_any(entries: List[Entry]) -> Dict[str, Any]:
    if not entries:
        raise ValueError("Input dataset is empty")

    spec = normalize_spec_contract(entries[0]["output"])
    spec["target"] = "structures"
    spec["conditions"]["proximity"]["object"] = "vegetation"
    spec["conditions"]["proximity"]["distance_meters"] = DEFAULT_DISTANCE_METERS
    spec["filters"] = {"min_height_meters": None, "min_cluster_size": None}
    spec["ranking"] = {"type": None, "top_n": None}
    spec["render"] = {"mode": "highlight", "show": ["structures", "vegetation", "encroachment"]}
    return spec


def classify_spec(spec: Dict[str, Any]) -> str:
    spec = normalize_spec_contract(spec)

    ranking_type = spec["ranking"].get("type")
    if ranking_type == "point_count":
        return "ranking_point_count"
    if ranking_type == "height":
        return "ranking_height"
    if ranking_type == "severity":
        return "ranking_severity"

    if spec["filters"].get("min_height_meters") is not None:
        return "filter_height"

    if spec["filters"].get("min_cluster_size") is not None:
        return "filter_cluster"

    show = spec["render"].get("show", [])
    if show == ["vegetation", "encroachment"]:
        return "render_vegetation_only"
    if show == ["structures", "encroachment"]:
        return "render_structures_only"
    if show == ["encroachment"]:
        return "render_encroachment_only"

    return "basic"


def group_entries_by_category(entries: List[Entry]) -> Dict[str, List[Entry]]:
    grouped = {category: [] for category in CATEGORY_RATIOS}

    for entry in entries:
        grouped[classify_spec(entry["output"])].append(entry)

    if not grouped["basic"]:
        grouped["basic"] = [
            {
                "input": "Show vegetation within 2 meters of structures",
                "output": basic_spec_from_any(entries),
            }
        ]

    return grouped


def progress_bar(current: int, total: int, width: int = 36) -> None:
    percent = min(100, int((current / total) * 100)) if total else 100
    filled = min(width, int(width * current / total)) if total else width
    bar = "█" * filled + "░" * (width - filled)
    print(f"\rGenerating dataset: [{bar}] {percent:3d}% ({current:,}/{total:,})", end="", flush=True)


def sample_distance() -> float:
    return random.choice(DEFAULT_DISTANCES_METERS)


def sample_distance_phrase(distance: float) -> Tuple[str, str, str]:
    distance_text = random.choice(distance_text_options(distance))
    unit = random.choice(units_for_distance_text(distance_text))
    return distance_text, unit, compact_unit(unit)


def common_slots(distance: float) -> Dict[str, str]:
    distance_text, unit, compact = sample_distance_phrase(distance)
    veg = random.choice(VEGETATION_TERMS)
    structure = random.choice(STRUCTURE_TERMS)
    issue = random.choice(ENCROACHMENT_TERMS)
    growth_phrase = (
        "are growing"
        if veg == "trees"
        else "is growing"
        if veg == "vegetation"
        else "exists"
    )

    return {
        "verb": random.choice(COMMAND_VERBS),
        "question": random.choice(QUESTION_PREFIXES),
        "veg_question": question_prefix_for_subject(veg),
        "issue_question": question_prefix_for_subject(issue),
        "structure_question": question_prefix_for_subject(structure),
        "veg": veg,
        "structure": structure,
        "issue": issue,
        "distance_text": distance_text,
        "unit": unit,
        "compact_unit": compact,
        "veg_is_are": verb_for_veg(veg),
        "structure_have": verb_for_structure(structure),
        "growth_phrase": growth_phrase,
    }


def vary_spec_for_category(category: str, seed_spec: Dict[str, Any], distance: float) -> Dict[str, Any]:
    if category in {"filter_cluster", "ranking_point_count"}:
        distance = random.choice([0.5, 1, 1.5, 2, 2.5, 3, 4, 5])

    spec = set_distance_meters(seed_spec, distance)

    spec["filters"] = {
        "min_height_meters": None,
        "min_cluster_size": None,
    }

    spec["ranking"] = {
        "type": None,
        "top_n": None,
    }

    spec["render"] = {
        "mode": "highlight",
        "show": ["structures", "vegetation", "encroachment"],
    }

    if category == "render_vegetation_only":
        spec["render"]["show"] = ["vegetation", "encroachment"]

    elif category == "render_structures_only":
        spec["render"]["show"] = ["structures", "encroachment"]

    elif category == "render_encroachment_only":
        spec["render"]["show"] = ["encroachment"]

    if category == "filter_height":
        spec["render"]["show"] = ["structures", "vegetation", "encroachment"]
        spec["filters"]["min_height_meters"] = random.choice([1, 2, 3, 5])

    elif category == "filter_cluster":
        spec["render"]["show"] = ["structures", "vegetation", "encroachment"]
        spec["filters"]["min_cluster_size"] = random.choice([10, 25, 50, 100])

    elif category == "ranking_point_count":
        spec["render"]["show"] = ["structures", "vegetation", "encroachment"]
        spec["ranking"]["type"] = "point_count"
        spec["ranking"]["top_n"] = random.choice([3, 5, 10])
        spec["filters"]["min_cluster_size"] = spec["filters"].get("min_cluster_size") or random.choice([25, 50, 100])

    elif category == "ranking_height":
        spec["render"]["show"] = ["structures", "vegetation", "encroachment"]
        spec["ranking"]["type"] = "height"
        spec["ranking"]["top_n"] = random.choice([3, 5, 10])
        spec["filters"]["min_height_meters"] = spec["filters"].get("min_height_meters") or random.choice([2, 3, 5])

    elif category == "ranking_severity":
        spec["render"]["show"] = ["structures", "vegetation", "encroachment"]
        spec["ranking"]["type"] = "severity"
        spec["ranking"]["top_n"] = random.choice([3, 5, 10])
        spec["filters"]["min_height_meters"] = spec["filters"].get("min_height_meters") or random.choice([2, 3, 5])
        spec["filters"]["min_cluster_size"] = spec["filters"].get("min_cluster_size") or random.choice([25, 50, 100])

    return spec


def generate_query_for_category(category: str, spec: Dict[str, Any], distance: float) -> Tuple[str, Dict[str, Any]]:
    slots = common_slots(distance)
    slots["height"] = str(spec.get("filters", {}).get("min_height_meters") or random.choice([1, 2, 3, 5]))
    slots["cluster_size"] = str(spec.get("filters", {}).get("min_cluster_size") or random.choice([10, 25, 50, 100]))
    slots["top_n"] = str(spec.get("ranking", {}).get("top_n") or random.choice([5, 10, 20]))

    query = clean_query(random.choice(CATEGORY_TEMPLATES[category]).format(**slots))

    if category == "filter_height" and not re.search(r"\bwithin\b", normalize_text(query)):
        spec["conditions"]["proximity"]["distance_meters"] = DEFAULT_DISTANCE_METERS
    spec = enforce_query_distance_rule(query, spec)

    return query, spec


def make_entry(input_text: str, output_spec: Dict[str, Any]) -> Entry:
    output_spec = enforce_query_distance_rule(input_text, output_spec)
    return {"input": clean_query(input_text), "output": output_spec}


def dedupe_entries(entries: Iterable[Entry]) -> List[Entry]:
    deduped: List[Entry] = []
    seen_inputs = set()

    for entry in entries:
        cleaned_input = clean_query(entry["input"])

        if is_bad_query(cleaned_input):
            continue

        normalized_input = normalize_text(cleaned_input)

        if normalized_input in seen_inputs:
            continue

        seen_inputs.add(normalized_input)

        cleaned_entry = {
            "input": cleaned_input,
            "output": enforce_query_distance_rule(cleaned_input, entry["output"]),
        }

        if "infrastructure" in normalize_text(cleaned_input) or "assets" in normalize_text(cleaned_input):
            continue

        deduped.append(cleaned_entry)

    return deduped


def category_targets(target_size: int, include_originals: bool, original_count: int) -> Dict[str, int]:
    remaining = max(0, target_size - (original_count if include_originals else 0))
    targets = {category: int(round(remaining * ratio)) for category, ratio in CATEGORY_RATIOS.items()}
    drift = remaining - sum(targets.values())
    targets["basic"] += drift
    return targets


def generate_feet_entry(category: str, seed_spec: Dict[str, Any]) -> Entry:
    feet = random.choice([1, 2, 3, 5, 6, 10, 15, 20, 25, 30, 50, 75, 100])
    meters = round(feet * 0.3048, 4)
    label = str(int(feet))
    foot_unit = "foot" if feet == 1 else "feet"
    spec = vary_spec_for_category(category, seed_spec, meters)

    structure = random.choice(STRUCTURE_TERMS)
    veg = random.choice(VEGETATION_TERMS)

    query = random.choice([
        f"Show {veg} within {label} {foot_unit} of {structure}",
        f"Highlight vegetation encroachment within {label} ft of {structure}",
        f"Find trees within {label} {foot_unit} of {structure}",
        f"Display {structure} with vegetation within {label} ft",
        f"Where are vegetation conflicts within {label} {foot_unit} of {structure}?",
    ])

    return make_entry(clean_query(query), spec)


def augment(entries: List[Entry], target_size: int, include_feet: bool, include_originals: bool) -> List[Entry]:
    grouped = group_entries_by_category(entries)
    targets = category_targets(target_size, include_originals, len(entries))
    augmented: List[Entry] = []

    total_estimated = (len(entries) if include_originals else 0) + sum(targets.values())
    progress_step = max(1, math.ceil(total_estimated / 100))
    generated_count = 0
    next_progress_at = progress_step

    def add_entry(entry: Entry) -> None:
        nonlocal generated_count, next_progress_at
        augmented.append(entry)
        generated_count += 1

        if generated_count >= next_progress_at or generated_count >= total_estimated:
            progress_bar(min(generated_count, total_estimated), total_estimated)
            next_progress_at += progress_step

    if include_originals:
        for entry in copy.deepcopy(entries):
            add_entry(normalize_seed_entry(entry))

    for category, target_count in targets.items():
        seed_entries = grouped.get(category) or grouped["basic"]

        feet_count = int(target_count * 0.08) if include_feet else 0
        meter_count = target_count - feet_count

        for _ in range(meter_count):
            seed_spec = copy.deepcopy(random.choice(seed_entries)["output"])
            distance = sample_distance()
            spec = vary_spec_for_category(category, seed_spec, distance)

            actual_distance = spec["conditions"]["proximity"]["distance_meters"]

            query, spec = generate_query_for_category(category, spec, actual_distance)
            add_entry(make_entry(query, spec))

        for _ in range(feet_count):
            seed_spec = copy.deepcopy(random.choice(seed_entries)["output"])
            add_entry(generate_feet_entry(category, seed_spec))

    print("\nDeduplicating and cleaning entries...")
    return dedupe_entries(augmented)


def write_jsonl(path: Path, entries: List[Entry]) -> None:
    with path.open("w", encoding="utf-8") as f:
        for entry in entries:
            f.write(json.dumps(entry, ensure_ascii=False, separators=(",", ":")) + "\n")


def main() -> None:
    args = parse_args()
    random.seed(args.seed)

    input_path = Path(args.input)
    output_path = Path(args.output)

    entries = load_jsonl(input_path)
    augmented = augment(entries, args.target_size, args.include_feet, args.include_originals)

    random.shuffle(augmented)
    write_jsonl(output_path, augmented)

    print(f"Read {len(entries)} entries from {input_path}")
    print(f"Wrote {len(augmented)} entries to {output_path}")


if __name__ == "__main__":
    main()
