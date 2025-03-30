FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir torch==2.3.1+cpu -f https://download.pytorch.org/whl/torch_stable.html

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY controller/app.py .
COPY scripts/config.py .
COPY terraquery_model_v3/config.json \
     terraquery_model_v3/generation_config.json \
     terraquery_model_v3/model.safetensors \
     terraquery_model_v3/special_tokens_map.json \
     terraquery_model_v3/tokenizer_config.json \
     terraquery_model_v3/spiece.model \
     /app/terraquery_model_v3/

EXPOSE 9090

CMD ["python", "app.py"]
