FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir torch==2.3.1+cpu -f https://download.pytorch.org/whl/torch_stable.html

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY controller/app.py .
COPY scripts/config.py .
COPY terraquery_model_v2/config.json \
     terraquery_model_v2/generation_config.json \
     terraquery_model_v2/model.safetensors \
     terraquery_model_v2/merges.txt \
     terraquery_model_v2/special_tokens_map.json \
     terraquery_model_v2/tokenizer_config.json \
     terraquery_model_v2/vocab.json \
     /app/terraquery_model_v2/

EXPOSE 9090

CMD ["python", "app.py"]
