#!/bin/bash

# Azure Deployment Script for Semantic Kernel Blueprint
# Requires: Azure CLI (az)

set -e

RESOURCE_GROUP="rg-semantic-kernel-blueprint"
LOCATION="eastus"

echo "🚀 Starting Azure Deployment..."

# 1. Create Resource Group
echo "Creating resource group: $RESOURCE_GROUP..."
az group create --name $RESOURCE_GROUP --location $LOCATION

# 2. Deploy Infrastructure (Initial pass to create ACR)
echo "Deploying Infrastructure..."

# Load API Key from .env
if [ -f .env ]; then
  OPENAI_KEY=$(grep OPENAI_API_KEY .env | cut -d '=' -f2)
fi

# We allow this to fail or warn if the image isn't built yet
az deployment group create \
  --resource-group $RESOURCE_GROUP \
  --template-file infra/main.bicep \
  --parameters openaiApiKey=$OPENAI_KEY \
  --no-wait

echo "Waiting for ACR to be ready..."
sleep 15

# Get the ACR Name (it should exist now even if the Container App revision failed)
ACR_NAME=$(az acr list --resource-group $RESOURCE_GROUP --query "[0].name" -o tsv)

if [ -z "$ACR_NAME" ]; then
    echo "❌ Failed to find Azure Container Registry. Checking deployment status..."
    exit 1
fi

# 3. Build and Push Docker Image (Local Build to bypass ACR Task restrictions)
echo "Building and pushing Docker image to $ACR_NAME..."

# Login to ACR
az acr login --name $ACR_NAME

IMAGE_URI="$ACR_NAME.azurecr.io/app-agent-api:latest"

docker build --platform linux/amd64 -t $IMAGE_URI .
docker push $IMAGE_URI

# 4. Final Deployment (to ensure Container App picks up the image and starts)
echo "Finalizing deployment..."
az deployment group create \
  --resource-group $RESOURCE_GROUP \
  --template-file infra/main.bicep \
  --parameters openaiApiKey=$OPENAI_KEY

echo "✅ Deployment Successful!"
echo "Your Agent API is being deployed to Azure Container Apps."
