FROM python:3.9-slim

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir torch==2.3.1+cpu -f https://download.pytorch.org/whl/torch_stable.html

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY terraquery_model/config.json \
     terraquery_model/generation_config.json \
     terraquery_model/model.safetensors \
     terraquery_model/merges.txt \
     terraquery_model/special_tokens_map.json \
     terraquery_model/tokenizer_config.json \
     terraquery_model/vocab.json \
     /app/terraquery_model/

EXPOSE 9090

CMD ["python", "app.py"]
