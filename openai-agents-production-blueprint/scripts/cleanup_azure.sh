#!/bin/bash

# Cleanup script for AutoGen Blueprint
# Deletes the resource group and all associated resources to ensure zero cost.

RESOURCE_GROUP="rg-autogen-blueprint"

echo "⚠️  WARNING: This will delete all Azure resources for the AutoGen Blueprint."
echo "Resource Group: $RESOURCE_GROUP"
echo ""

# Check if resource group exists
if az group exists --name $RESOURCE_GROUP &> /dev/null; then
    echo "🗑️  Deleting Resource Group: $RESOURCE_GROUP..."
    az group delete --name $RESOURCE_GROUP --yes --no-wait
    echo "✅ Deletion initiated. This may take a few minutes to complete in the background."
    echo "You can check progress in the Azure Portal or by running: az group show -n $RESOURCE_GROUP"
else
    echo "ℹ️  Resource Group $RESOURCE_GROUP does not exist. Nothing to clean up."
fi
