FROM python:3.12-slim

WORKDIR /app

RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip

COPY app/app.py .

EXPOSE 8080

CMD ["python", "app.py"]FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip

COPY app/app.py .

EXPOSE 8080

CMD ["python", "app.py"]FROM python:3.12-slim

WORKDIR /app

COPY app/app.py .

EXPOSE 8080

CMD ["python", "app.py"]
