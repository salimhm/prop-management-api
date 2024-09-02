FROM python:3.10-slim

RUN mkdir /app

WORKDIR /app

COPY . /app/

RUN pip install -r requirements.txt

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=property_management.settings
ENV PYTHONUNBUFFERED=1

RUN python manage.py makemigrations

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
