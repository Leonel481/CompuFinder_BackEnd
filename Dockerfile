FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /Back_End_app

WORKDIR /Back_End_app

COPY . /Back_End_app

# Copia el script al contenedor
COPY start-django.sh /usr/local/bin/start-django.sh

# Establece permisos de ejecución
RUN chmod +x /usr/local/bin/start-django.sh

RUN pip install --no-cache-dir -r requirements.txt