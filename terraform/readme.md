# 💠 Infraestructura: VM Ubuntu + PostgreSQL + Docker + Django

Este proyecto utiliza **Terraform** para desplegar una infraestructura automatizada en **Google Cloud Platform (GCP)**. 
Crea las reglas de **firewall** y las **IPs** que usara la **máquina virtual**.
Posteriormente, crea una **máquina virtual con Ubuntu**, que instala automáticamente **Docker**, **PostgreSQL**, y despliega una **aplicación Django** mediante Docker Compose.

---

## 📦 Estructura del Proyecto
. 
├── main.tf # Infraestructura principal 
├── provider.tf # Provider nube Utilizado
├── variables.tf # Declaración de variables 
├── terraform.tfvars.template # Plantilla de las variables
├── init_vm.sh # Script de inicialización de la VM 
└── README.md

## Service Acount
Obtener el service acount del proveedor para que terraform pueda conectarse y crear los servicios que requiere la infraestructura

## Iniciar la creacion de los servicion
```bash
cd terraform/
terraform init
terraform plan
terraform apply
terraform destroy # Solo para destruir los servicios creados
```

## Verificaciones en la VM
```bash
sudo systemctl status postgresql # Verificar la isntalacion de postgresql y ver el estado actual
docker --version
docker-compose --version
```