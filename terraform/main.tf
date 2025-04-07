# Este código es compatible con Terraform 4.25.0 y versiones compatibles con 4.25.0.
# Para obtener información sobre la validación de este código de Terraform, consulta https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/google-cloud-platform-build#format-and-validate-the-configuration

# Firewall Rule DataaBase BackEnd
resource "google_compute_firewall" "allow_postgresql" {
  name    = "allow-postgresql"
  network = var.network  # Usa la variable para la red

  allow {
    protocol = "tcp"
    ports    = [var.postgresql_port]  # Usa la variable para el puerto de PostgreSQL
  }

  # Permitir acceso desde otras VM en la misma red
  source_ranges = ["10.128.0.0/20"]
  target_tags   = ["postgresql-server"]  
}

# Static Ip internal
resource "google_compute_address" "static_internal_ip" {
  name   = var.ip_internal_name
  region = var.gcp_region 
  address_type = "INTERNAL" 
  address = "10.128.0.2" 
  subnetwork = "projects/${var.gcp_project}/regions/${var.gcp_region}/subnetworks/default"  
}

# Static Ip External
resource "google_compute_address" "static_external_ip" {
  name   = var.ip_external_name
  region = var.gcp_region
  address_type = "EXTERNAL" 
}

data "google_compute_image" "ubuntu" {
  family  = "ubuntu-2204-lts"
  project = "ubuntu-os-cloud"
}

# Virtual Machine for BackEnd
resource "google_compute_instance" "vm-001-prod-scp-backend-uscentral" {
  boot_disk {
    auto_delete = true
    device_name = var.vm_name

    initialize_params {
      image = data.google_compute_image.ubuntu.self_link
      size  = var.boot_disk_size
      type  = "pd-balanced"
    }

    mode = "READ_WRITE"
  }

  can_ip_forward      = false
  deletion_protection = false
  enable_display      = false

  labels = {
    goog-ec-src       = "vm_add-tf"
  }

  machine_type = var.vm_machine_type
  name         = var.vm_name
  zone         = var.zone

  network_interface {
    access_config {
      nat_ip       = google_compute_address.static_external_ip.address
      network_tier = "PREMIUM"
    }

    network_ip  = google_compute_address.static_internal_ip.address
    queue_count = 0
    stack_type  = "IPV4_ONLY"
    subnetwork  = "projects/${var.gcp_project}/regions/${var.gcp_region}/subnetworks/default"  
  }

  scheduling {
    automatic_restart   = true
    on_host_maintenance = "MIGRATE"
    preemptible         = false
    provisioning_model  = "STANDARD"
  }

  service_account {
    email  = var.service_account
    scopes = ["https://www.googleapis.com/auth/devstorage.read_only", 
              "https://www.googleapis.com/auth/logging.write", 
              "https://www.googleapis.com/auth/monitoring.write", 
              "https://www.googleapis.com/auth/service.management.readonly", 
              "https://www.googleapis.com/auth/servicecontrol", 
              "https://www.googleapis.com/auth/trace.append"]
  }

  shielded_instance_config {
    enable_integrity_monitoring = true
    enable_secure_boot          = false
    enable_vtpm                 = true
  }

  depends_on = [google_compute_address.static_external_ip, google_compute_address.static_internal_ip]


  tags = ["http-server", "https-server", "postgresql-server"]
  
  metadata_startup_script = templatefile("${path.module}/init_vm.sh", {
    USER = var.USER
    vm_user_global = var.vm_user_global
    vm_user_pass_global = var.vm_user_pass_global
    postgresql_username = var.postgresql_username
    postgresql_password = var.postgresql_password
    db_dev = var.db_dev
    df_prod = var.df_prod
    ip_infra_24 = var.ip_infra_24
    ip_docker = var.ip_docker
    ip_leo = var.ip_leo_24
    ip_moreno = var.ip_moreno_24
  })
}