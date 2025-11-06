#!/bin/bash
./scripts/update_config.sh

echo "----- Running backend webserver -----"
python src/app.py