#!/bin/bash

# Load values from JSON
CONFIG_FILE="config.json"

# Get values from config file and set to environment vars 
export API_HOST=$(jq -r '.api_host' "$CONFIG_FILE")
export API_PORT=$(jq -r '.api_port' "$CONFIG_FILE")
export DB_HOST=$(jq -r '.db_host' "$CONFIG_FILE")
export VERSION=$(jq -r '.version' "$CONFIG_FILE")
export VITE_API_URL="http://$API_HOST:$API_PORT"
export PORTAINER_URL="http://$PORTAINER_HOST:$PORTAINER_PORT"
export ENDPOINT_ID=1

# Update the JSON file with sensitive credentials
jq --arg db_user "$SQL_DB_USR" \
   --arg db_password "$SQL_DB_PSW" \
   --arg jwt_token "$JWT_TOKEN" \
   '.db_user = $db_user | .db_password = $db_password | .jwt_token = $jwt_token' \
   config.json > tmp.json && mv tmp.json config.json


# Write them to globals.env
{
  echo "export API_HOST=\"$API_HOST\""
  echo "export API_PORT=\"$API_PORT\""
  echo "export DB_HOST=\"$DB_HOST\""
  echo "export VERSION=\"$VERSION\""
  echo "export PORTAINER_URL=\"$PORTAINER_URL\""
  echo "export ENDPOINT_ID=\"$ENDPOINT_ID\""
} > ./globals.env

source ./globals.env