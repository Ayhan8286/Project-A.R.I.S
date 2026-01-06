# Milestone 7: Control Center

This directory contains the "Control Center" configuration, providing user interfaces for managing the AI infrastructure.

## Services

### Portainer (Container Management)
*   **URL:** `http://<YOUR_SERVER_IP>:9000`
*   **Purpose:** Visual management of Docker containers, volumes, and networks.
*   **First Run:** You will be prompted to create an admin password.

### Streamlit (Mission Control Dashboard)
*   **URL:** `http://<YOUR_SERVER_IP>:8501`
*   **Purpose:** A custom "Mission Control" UI to monitor system status and AI agents.
*   **Source Code:** Located in `07-Control-Center/dashboard/app.py`.

## Deployment

These services are deployed as part of the main `docker-compose.yml` stack in the `03-Data-Spine` directory.

To update and start the new services:

```bash
cd 03-Data-Spine
docker compose up -d
```
