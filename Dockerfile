FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app/src

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

CMD python manage.py migrate \
    && python manage.py load_data uszips.csv \
    && python manage.py runserver 0.0.0.0:8000