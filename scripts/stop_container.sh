#!/bin/bash
source ~/globals.env
source ~/.portainer_token.env


# Get all containers
containers=$(curl -s -X GET "$PORTAINER_URL/api/endpoints/$ENDPOINT_ID/docker/containers/json" \
  -H "Authorization: Bearer $PORTAINER_TOKEN")

# Filter by name prefix
CONTAINER_ID=$(echo "$containers" | jq -r '.[] | select(.Names[] | test("^/lagersystem-container")) | .Id')

echo "Container ID: $CONTAINER_ID"

status_code=$(curl -s -o /dev/null -w "%{http_code}" -X POST \
  "$PORTAINER_URL/api/endpoints/$ENDPOINT_ID/docker/containers/$CONTAINER_ID/stop" \
  -H "Authorization: Bearer $PORTAINER_TOKEN")


if [ "$status_code" -eq 204 ]; then
  echo "Container stopped successfully."
else
  echo "Failed to stop container. Status: $status_code"
fi
