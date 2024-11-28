#!/bin/sh

# Esperar a que Nginx esté listo
sleep 15

# Obtener certificados iniciales
certbot certonly --webroot --webroot-path=/var/www/certbot -d ${DOMAIN} -d www.${DOMAIN} --non-interactive --agree-tos --email ${EMAIL}

# Iniciar el proceso de renovación
trap exit TERM; while :; do 
    certbot renew
    sleep 12h
done