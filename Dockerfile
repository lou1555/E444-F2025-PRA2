FROM python:3.11-slim

# good container defaults
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# install deps first (layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy the app
COPY . .

# Flask runtime config
ENV FLASK_APP=run.py \
    FLASK_RUN_HOST=0.0.0.0 \
    FLASK_RUN_PORT=5000

# (optional) document the port
EXPOSE 5000

# start the app
CMD ["python", "-m", "flask", "run"]
