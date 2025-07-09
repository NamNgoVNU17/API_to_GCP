#!/bin/bash
set -e

pip install -r /requirements.txt

sleep 10

airflow db upgrade


airflow users create \
  --username admin \
  --firstname Nam \
  --lastname Ngo \
  --role Admin \
  --email nam@example.com \
  --password admin


airflow webserver & airflow scheduler
