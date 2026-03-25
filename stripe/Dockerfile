FROM python:3.11.5-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP=server.py
CMD ["python3", "server.py"]