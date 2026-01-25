resource "google_cloud_run_v2_service" "engine" {
  name     = var.service_name
  location = var.region
  ingress  = "INGRESS_TRAFFIC_ALL"

  template {
    service_account = google_service_account.agent_engine.email
    containers {
      image = "gcr.io/${var.project_id}/${var.service_name}:${var.image_tag}"
      
      env {
        name  = "GOOGLE_API_KEY"
        value = var.google_api_key
      }
      
      ports {
        container_port = 8000
      }

      resources {
        limits = {
          cpu    = "2"
          memory = "2Gi"
        }
      }
    }
  }
}

# Allow unauthenticated access (public) - change to internal if needed
resource "google_cloud_run_v2_service_iam_member" "noauth" {
  location = google_cloud_run_v2_service.engine.location
  name     = google_cloud_run_v2_service.engine.name
  role     = "roles/run.invoker"
  member   = "allUsers"
}
