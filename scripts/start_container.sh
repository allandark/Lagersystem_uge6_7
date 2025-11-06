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


# Check for success
container_id=$(echo "$body" | jq -r '.Id // empty')
error_message=$(echo "$body" | jq -r '.message // empty')

if [ "$status_code" -eq 201 ] && [ -n "$container_id" ]; then
  echo "Container created successfully: $container_id"
else
  echo "Failed to create container. Status: $status_code"
  echo "Error: $error_message"
  exit 1
fi

