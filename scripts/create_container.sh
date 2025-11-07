#!/bin/bash
source ./globals.env
source ./.portainer_token.env

# Get all containers
containers=$(curl -s -X GET "$PORTAINER_URL/api/endpoints/$ENDPOINT_ID/docker/containers/json?all=true" \
  -H "Authorization: Bearer $PORTAINER_TOKEN")

# Filter by name prefix
CONTAINER_ID=$(echo "$containers" | jq -r --arg prefix "/$CONTAINER_NAME-container" '
  .[] 
  | select(.Names[]? | startswith($prefix)) 
  | .Id
')
echo "Container ID: $CONTAINER_ID"

# Delete request for running container
status_code=$(curl -s -o /dev/null -w "%{http_code}" -X DELETE "$PORTAINER_URL/api/endpoints/$ENDPOINT_ID/docker/containers/$CONTAINER_ID?force=true" \
  -H "Authorization: Bearer $PORTAINER_TOKEN")

if [ "$status_code" -eq 204 ]; then
  echo "Container deleted successfully."
else
  echo "Failed to delete container. Status: $status_code"
fi

# Post request for create container
response=$(curl -s -w "HTTPSTATUS:%{http_code}" -X POST "$PORTAINER_URL/api/endpoints/$ENDPOINT_ID/docker/containers/create?name=$CONTAINER_NAME-container-$VERSION" \
  -H "Authorization: Bearer $PORTAINER_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "Image": "'"$CONTAINER_NAME:$VERSION"'",
    "HostConfig": {
      "PortBindings": {
        "'"$CONTAINER_PORT"'/tcp": [
          {
            "HostPort": "'"$CONTAINER_PORT"'"
          }
        ]
      },
      "NetworkMode": "bridge"
    },
    "ExposedPorts": {
      "'"$CONTAINER_PORT"'/tcp": {}
    }
  }')

# Extract body and status
body=$(echo "$response" | sed -e 's/HTTPSTATUS\:.*//g')
status_code=$(echo "$response" | tr -d '\n' | sed -e 's/.*HTTPSTATUS://')


# Check for success
container_id=$(echo "$body" | jq -r '.Id // empty')
error_message=$(echo "$body" | jq -r '.message // empty')

if [ "$status_code" -eq 200 ] && [ -n "$container_id" ]; then
  echo "Container created successfully: $container_id"
else
  echo "Failed to create container. Status: $status_code"
  echo "Error: $error_message"
  exit 1
fi
