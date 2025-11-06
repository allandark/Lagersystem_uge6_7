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
  -d "{
    \"Image\": \"$CONTAINER_NAME:$VERSION\",
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

# Extract body and status
body=$(echo "$response" | sed -e 's/HTTPSTATUS\:.*//g')
status_code=$(echo "$response" | tr -d '\n' | sed -e 's/.*HTTPSTATUS://')

# Check creation status
if [ "$status_code" -eq 201 ]; then
  echo "Container created successfully."
else
  echo "Failed to create container. Status: $status_code"
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


