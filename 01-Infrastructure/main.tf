terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

provider "google" {
  project = "your-project-id"
  region  = "us-central1"
  zone    = "us-central1-a"
}

resource "google_compute_instance" "vm_instance" {
  name         = "milestone1-vm"
  machine_type = "e2-standard-8"
  tags         = ["http-server"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"
    access_config {
    }
  }
}

resource "google_compute_firewall" "default" {
  name    = "milestone2-firewall"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["80", "443", "5678", "8080", "3000", "8501", "8000", "9000"]
  }

  target_tags = ["http-server"]
  source_ranges = ["0.0.0.0/0"]
}
