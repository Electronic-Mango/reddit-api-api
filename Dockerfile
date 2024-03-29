# Dockerfile which can be used for deploying the API as a Docker container.

FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY *.yml .

CMD ["python", "src/main.py"]
