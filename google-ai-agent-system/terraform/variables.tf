variable "project_id" {
  description = "The Google Cloud Project ID"
  type        = string
}

variable "region" {
  description = "The GCN region to deploy to"
  type        = string
  default     = "us-central1"
}

variable "service_name" {
  description = "The name of the Cloud Run service"
  type        = string
  default     = "google-ai-agent-engine"
}

variable "image_tag" {
  description = "The container image tag to deploy"
  type        = string
  default     = "latest"
}

variable "google_api_key" {
  description = "Google API Key for Gemini/ADK (passed as env var)"
  type        = string
  sensitive   = true
}
