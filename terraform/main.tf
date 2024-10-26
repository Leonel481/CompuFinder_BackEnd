# This code is compatible with Terraform 4.25.0 and versions that are backwards compatible to 4.25.0.
# For information about validating this Terraform code, see https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/google-cloud-platform-build#format-and-validate-the-configuration

resource "google_compute_instance" "vm-001-prod-scp-backend-uscentral" {
  boot_disk {
    auto_delete = true
    device_name = "vm-001-prod-scp-uscentral"

    initialize_params {
      image = "projects/ubuntu-os-cloud/global/images/ubuntu-2204-jammy-v20240927"
      size  = 20
      type  = "pd-balanced"
    }

    mode = "READ_WRITE"
  }

  can_ip_forward      = false
  deletion_protection = false
  enable_display      = false

  labels = {
    goog-ec-src = "vm_add-tf"
  }

  machine_type = "e2-medium"
  name         = "vm-001-prod-scp-backend-uscentral"

  network_interface {
    access_config {
      nat_ip       = "35.226.28.41"
      network_tier = "PREMIUM"
    }

    network_ip  = "10.128.0.2"
    queue_count = 0
    stack_type  = "IPV4_ONLY"
    subnetwork  = "projects/project-compu-finder-01/regions/us-central1/subnetworks/default"
  }

  scheduling {
    automatic_restart   = true
    on_host_maintenance = "MIGRATE"
    preemptible         = false
    provisioning_model  = "STANDARD"
  }

  shielded_instance_config {
    enable_integrity_monitoring = true
    enable_secure_boot          = false
    enable_vtpm                 = true
  }

  tags = ["http-server", "https-server", "lb-health-check"]
  zone = "us-central1-f"
}

