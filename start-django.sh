#!/bin/sh

# Hacer las migraciones
echo "Ejecutando makemigrations..."
python manage.py makemigrations

echo "Ejecutando migrate..."
python manage.py migrate

# Recoger archivos estáticos
echo "Ejecutando collectstatic..."
python manage.py collectstatic --noinput

# Iniciar el servidor Django con Gunicorn
echo "Iniciando el servidor Django con Gunicorn..."
exec gunicorn -c config/gunicorn/conf.py --bind :8000 --chdir myproject myproject.wsgi:application

