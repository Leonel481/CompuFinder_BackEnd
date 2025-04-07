#!/bin/bash
# startup_script.sh

# Actualizar el sistema
apt-get update
apt-get upgrade -yq

# Instalar depedencias para el Backend
apt-get install -yq python3-pip python3-dev python3-venv

# Instalar paquetes necesarios para Docker
sudo apt update
sudo apt install -yq apt-transport-https ca-certificates curl software-properties-common

# Importar la clave GPG de Docker y agregar repositorio
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - 
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu `lsb_release -cs` stable" 

# Instalar Docker
apt-get install -yq docker-ce docker-ce-cli

# Configurar permisos de Docker
sudo groupadd docker || true
sudo usermod -aG docker "${USER}"

# Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Crear usuario ubuntu universal
adduser --disabled-password --gecos "" "${vm_user_global}"
echo "${vm_user_global}:${vm_user_pass_global}" | chpasswd
usermod -aG sudo "${vm_user_global}"
usermod -aG docker "${vm_user_global}" 

# Instalar PostgreSQL
sudo apt-get install -yq postgresql postgresql-contrib

sudo systemctl enable postgresql
sudo systemctl start postgresql

sudo -u postgres psql <<-"EOF"
CREATE USER ${postgresql_username} WITH ENCRYPTED PASSWORD '${postgresql_password}';

CREATE DATABASE ${db_dev};
GRANT ALL PRIVILEGES ON DATABASE ${db_dev} TO ${postgresql_username};

CREATE DATABASE ${df_prod};
GRANT ALL PRIVILEGES ON DATABASE ${df_prod} TO ${postgresql_username};
EOF

# Modificar los archivos de configuracion de PostgreSQL con las IPs redes de la infraestructura
sudo sed -i "s/^#listen_addresses = 'localhost'/listen_addresses = '*'/g" /etc/postgresql/*/main/postgresql.conf
sudo sed -i "s/local   all             all                                     peer/local   all             all                                     md5/g" /etc/postgresql/*/main/pg_hba.conf
sudo echo "host    all             all             "${ip_infra_24}"             md5" >> /etc/postgresql/*/main/pg_hba.conf
sudo echo "host    all             all             "${ip_docker}"             md5" >> /etc/postgresql/*/main/pg_hba.conf
sudo echo "host    all             all             "${ip_leo}"             md5" >> /etc/postgresql/*/main/pg_hba.conf
sudo echo "host    all             all             "${ip_moreno}"             md5" >> /etc/postgresql/*/main/pg_hba.conf

sudo systemctl restart postgresql

echo "=== Startup script completed successfully ==="