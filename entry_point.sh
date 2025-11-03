#!/bin/bash
./update_config.sh
echo "----- Installing Frontend distribution -----"
cd lager-frontend
npm install
npm run build
# ls -la ./dist
cd ..
echo "----- Running backend webserver -----"
python src/app.py