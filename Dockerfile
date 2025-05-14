FROM python:3.11-slim

WORKDIR /app

COPY server.py requirements.txt .env . ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "server.py"]
