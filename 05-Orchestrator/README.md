# Milestone 5: Orchestrator

This directory contains the setup for the project's orchestrator using Apache Airflow.

## Installation Commands

Run the following commands to set up and start Airflow:

```bash
mkdir -p ~/gtm-engine/airflow

curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.9.1/docker-compose.yaml'

echo -e "AIRFLOW_UID=$(id -u)" > .env

docker compose up airflow-init

docker compose up -d
```
