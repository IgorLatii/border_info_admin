FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential libpq-dev && apt-get clean

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Perform static collection and migrations when starting a container
CMD ["bash", "-c", "python manage.py collectstatic --noinput && python manage.py migrate && gunicorn admin_panel.wsgi:application --bind 0.0.0.0:8001"]
