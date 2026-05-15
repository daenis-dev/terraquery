# TerraQuery

Point cloud analysis powered by natural language.

Project includes everything needed to train a small language model locally, as well as all files needed to run the web application locally.

The only thing that is not included are the demo tiles; send me a message if you would like access to these.

## Training the Model

Download the required dependencies
```
pip install \
  torch \
  transformers \
  scikit-learn \
  numpy \
  sentencepiece \
  accelerate
```
Augment the seed data
```
python3 data_augment.py
```
Train the model
```
python3 train_flan_t5_small.py
```

## Running the TerraQuery Application

Build the LiDAR Analysis API
```
docker build --no-cache --platform linux/amd64 -t terraquery-api -f terraquery-api/Dockerfile .
```
Run the LiDAR Analysis API
```
docker run --rm -it \
    --platform linux/amd64 \                           
    -p 8080:8080 \
    -v "$(pwd)":/data \
    -e KY_TILE_INDEX_URL="https://opendata.arcgis.com/datasets/b3a74b4e740847a1b9272d40100d9d60_0.geojson" \
    terraquery-api
```
Run the LiDAR Spec Generation API
```
cd spec-generator-model && uvicorn inference_server:app --host 0.0.0.0 --port 8000
```
Run the TerraQuery web client
```
npx http-server . -p 4200 --cors
```

## Architecture Overview

![TerraQuery Architecture](architecture.png)