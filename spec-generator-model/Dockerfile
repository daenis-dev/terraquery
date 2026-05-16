FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir \
    fastapi \
    uvicorn \
    transformers \
    sentencepiece \
    accelerate

RUN pip install --no-cache-dir \
    --index-url https://download.pytorch.org/whl/cpu \
    torch

COPY . .

EXPOSE 8000

CMD ["uvicorn", "inference_server:app", "--host", "0.0.0.0", "--port", "8000"]