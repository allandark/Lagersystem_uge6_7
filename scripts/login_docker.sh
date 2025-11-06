#!/bin/bash

# Portainer credentials
USERNAME="${PORTAINER_USR}"
PASSWORD="${PORTAINER_PSW}"


# Authenticate and get JWT token
export TOKEN=$(curl -s -X POST "$PORTAINER_URL/api/auth" \
  -H "Content-Type: application/json" \
  -d "{\"Username\":\"$USERNAME\",\"Password\":\"$PASSWORD\"}" | jq -r .jwt)

echo "JWT Token: $TOKEN"
echo "export PORTAINER_TOKEN=$TOKEN" > ~/.portainer_token.env