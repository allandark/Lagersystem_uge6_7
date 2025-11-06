#!/bin/bash
source ~/globals.env
source ~/.portainer_token.env

# Get all containers
containers=$(curl -s -X GET "$PORTAINER_URL/api/endpoints/$ENDPOINT_ID/docker/containers/json?all=true" \
  -H "Authorization: Bearer $PORTAINER_TOKEN")

# Filter by name prefix
CONTAINER_ID=$(echo "$containers" | jq -r '.[] | select(.Names[] | test("^/lagersystem-container")) | .Id')

echo "Container ID: $CONTAINER_ID"

status_code=$(curl -s -o /dev/null -w "%{http_code}" -X DELETE "$PORTAINER_URL/api/endpoints/$ENDPOINT_ID/docker/containers/$CONTAINER_ID?force=true"\
    -H "Authorization: Bearer $PORTAINER_TOKEN")

if [ "$status_code" -eq 204 ]; then
  echo "Container deleted successfully."
else
  echo "Failed to delete container. Status: $status_code"
fi


status_code=$(curl -s -X POST "$PORTAINER_URL/api/endpoints/$ENDPOINT_ID/docker/containers/create?name=lagersystem-container" \
  -H "Authorization: Bearer $PORTAINER_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{
    \"Image\": \"$CONTAINER_NAME\",
    \"HostConfig\": {
      \"PortBindings\": {
        \"$CONTAINER_PORT/tcp\": [
          {
            \"HostPort\": \"$CONTAINER_PORT\"
          }
        ]
      },
      \"NetworkMode\": \"bridge\"
    },
    \"ExposedPorts\": {
      \"$CONTAINER_PORT/tcp\": {}
    }
  }")


if [ "$status_code" -eq 201 ]; then
  echo "Container created successfully."
else
  echo "Failed to create container. Status: $status_code"
fi
