resource "google_service_account" "agent_engine" {
  account_id   = "ai-agent-engine-sa"
  display_name = "Service Account for Google AI Agent Engine"
}

resource "google_project_iam_member" "logging" {
  project = var.project_id
  role    = "roles/logging.logWriter"
  member  = "serviceAccount:${google_service_account.agent_engine.email}"
}

resource "google_project_iam_member" "monitoring" {
  project = var.project_id
  role    = "roles/monitoring.metricWriter"
  member  = "serviceAccount:${google_service_account.agent_engine.email}"
}
