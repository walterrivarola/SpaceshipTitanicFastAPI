FROM python:3.11-slim

RUN pip install fastapi pandas numpy

COPY. /app
WORKDIR /app

COPY src/modelo_entrenado.pkl /app/src/modelo_entrenado.pkl

CMD ["uvicorn", "app:app", "--host", "127.0.0.1", "--port", "8000", "--reload"]