FROM python:3.10

WORKDIR /app

COPY requirements.txt .
COPY api_server.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "api_server.py"]
