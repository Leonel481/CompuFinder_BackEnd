variable "gcp_scp_key" {
    description = "GCP service account key file"
    type = string
}

variable "gcp_project" {
    description = "GCP project ID"
    type = string
}

variable "gcp_region" {
    description = "GCP Region"
    type = string
}

variable "service_account" {
    description = "Service account"
    type = string
}

variable "USER" {
    description = "User gcp"
    type = string
}

variable "vm_user_global" {
    description = "New user for virtual machine"
    type = string
}

variable "vm_user_pass_global" {
    description = "New user pass for virtual machine"
    type = string
}

variable "postgresql_username" {
    description = "User for postgresql"
    type = string
}

variable "postgresql_password" {
    description = "Pass for postgresql"
    type = string
}

variable "db_dev" {
    description = "Database for develop"
    type = string
}

variable "df_prod" {
    description = "Database for production app"
    type = string
}

variable "ip_infra_24" {
    description = "IP for another vms /24"
    type = string
}

variable "ip_leo_24" {
    description = "ip local user/24"
    type = string
}

variable "ip_moreno_24" {
    description = "ip local user2/24"
    type = string
}

variable "ip_docker" {
    description = "ip for network docker"
    type = string
}


variable "vm_name" {
    description = "instance name"
    type = string
}

variable "vm_machine_type" {
  description = "Machine type for the VM"
  type        = string
}

variable "boot_disk_size" {
  description = "Boot disk size in GB"
  type        = number
  default     = 20
}

variable "zone" {
  description = "zone configuration"
  type = string
}

variable "network" {
  description = "Network for the VM"
  type        = string
  default     = "default"
}

variable "postgresql_port" {
  description = "Port for PostgreSQL"
  type        = number
  default     = 5432
}

variable "ip_internal_name" {
    description = "Ip internal name"
    type = string
    default = "scp-internal-backend"
}

variable "ip_external_name" {
    description = "Ip external name"
    type = string
    default = "scp-external-backend"
}