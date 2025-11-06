#!/bin/bash
source ~/globals.env
source ~/.portainer_token.env


# Get all containers
containers=$(curl -s -X GET "$PORTAINER_URL/api/endpoints/$ENDPOINT_ID/docker/containers/json?all=true" \
  -H "Authorization: Bearer $PORTAINER_TOKEN")

# Filter by name prefix
CONTAINER_ID=$(echo "$containers" | jq -r '.[] | select(.Names[] | test("^/lagersystem-container")) | .Id')
echo "Container ID: $CONTAINER_ID"

status_code=$(curl -s -o /dev/null -w "%{http_code}" -X POST \
  "$PORTAINER_URL/api/endpoints/$ENDPOINT_ID/docker/containers/$CONTAINER_ID/start" \
  -H "Authorization: Bearer $PORTAINER_TOKEN")



if [ "$status_code" -eq 204 ]; then
  echo "Container started successfully."
else
  echo "Failed to start container. Status: $status_code"
fi

# Get container details
container_info=$(curl -s -X GET "$PORTAINER_URL/api/endpoints/$ENDPOINT_ID/docker/containers/$CONTAINER_ID/json" \
  -H "Authorization: Bearer $PORTAINER_TOKEN")
  
# Extract the status
status=$(echo "$container_info" | jq -r '.State.Status')

# Check if it's running
if [ "$status" != "running" ]; then
  echo "Container is not running. Status: $status"
  exit 1
else
  echo "Container is running."
fi

