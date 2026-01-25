# Infra-as-Code (Terraform)

This directory contains the Terraform configuration for deploying the **Google AI Agent System** to Google Cloud Platform.

## 🚀 Deployment Steps

1. **Install Terraform**: Ensure you have [Terraform](https://www.terraform.io/downloads.html) installed locally.
2. **GCP Auth**: Log in to your Google Cloud project:
   ```bash
   gcloud auth application-default login
   ```
3. **Setup Variables**:
   Copy `terraform.tfvars.example` to `terraform.tfvars` and fill in your values:
   ```bash
   cp terraform.tfvars.example terraform.tfvars
   ```
4. **Initialize**:
   ```bash
   terraform init
   ```
5. **Plan & Apply**:
   ```bash
   terraform plan
   terraform apply
   ```

## 🏗 Resources Created

- **Google Cloud Run**: Deploys the FastAPI engine as a serverless container.
- **IAM Service Account**: A dedicated service account with minimal permissions (`logging.logWriter`, `monitoring.metricWriter`).
- **IAM Policy**: Configures the service to be publicly accessible (can be restricted in `cloud_run.tf`).

## 🐳 Containerization Note

Before applying, ensure you have built and pushed your container image to Google Container Registry (GCR) or Artifact Registry:

```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/google-ai-agent-engine .
```
