#!/bin/bash

# # Reemplaza las variables de entorno en el archivo de plantilla y genera el archivo de configuración
# envsubst < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf

# # Reemplaza las barras invertidas para que Nginx pueda interpretar correctamente las variables
# sed -i 's/\\\$/\$/g' /etc/nginx/conf.d/default.conf

# # Inicia Nginx
# exec nginx -g 'daemon off;'


# Cargar las variables desde el archivo .env
set -a
source .env
set +a

# Eliminar barras invertidas del archivo de configuración y guardar en un nuevo archivo
sed 's/\\//g' /etc/nginx/conf.d/nginx.conf.template > /etc/nginx/conf.d/nginx.conf

# Reemplazar solo la variable SERVER_NAME en el nuevo archivo
sed -i "s/\${SERVER_NAME}/${SERVER_NAME}/" /etc/nginx/conf.d/nginx.conf

# Iniciar Nginx
nginx -g 'daemon off;'