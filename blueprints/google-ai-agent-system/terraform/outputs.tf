output "service_url" {
  description = "The URL of the deployed Cloud Run service"
  value       = google_cloud_run_v2_service.engine.uri
}

output "service_account_email" {
  description = "The email of the service account used by the engine"
  value       = google_service_account.agent_engine.email
}
