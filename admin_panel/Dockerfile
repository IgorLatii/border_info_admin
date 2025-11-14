FROM python:3.10-slim

WORKDIR /app


RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .


RUN pip install --no-cache-dir -r requirements.txt


COPY . .

CMD ["bash", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn admin_panel.wsgi:application --bind 0.0.0.0:8001"]
