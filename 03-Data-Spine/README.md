# Milestone 3: Data Spine

This directory contains the Docker Compose configuration to set up the data spine for the project, including PostgreSQL, Redis, and n8n.

## Prerequisites

- Docker and Docker Compose installed (completed in Milestone 2).

## Instructions

### 1. Create the .env File

Create a file named `.env` in the `03-Data-Spine` directory with the following content. Replace the placeholder values with your desired credentials.

```bash
POSTGRES_USER=n8n
POSTGRES_PASSWORD=securepassword123
POSTGRES_DB=n8n_db
N8N_ENCRYPTION_KEY=somerandomencryptionkey
```

### 2. Run the Services

Navigate to the directory and start the services using Docker Compose:

```bash
cd 03-Data-Spine
docker compose up -d
```

### 3. Verify Installation

-   **n8n:** Open your browser and navigate to `http://<YOUR_SERVER_IP>:5678`.
-   **PostgreSQL:** Accessible on port `5432`.
-   **Redis:** Accessible on port `6379`.
