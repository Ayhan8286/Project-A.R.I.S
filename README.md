# GTM Engine

The GTM Engine is a comprehensive production-ready stack for AI Agents, Data Processing, and Orchestration.

## 📂 Project Structure

*   `terraform/`: Infrastructure as Code (GCP).
*   `deploy/`: Docker Compose and deployment scripts.
*   `src/`: Source code for Agents, Dashboard, and Utilities.
    *   `dashboard/`: Streamlit Mission Control App.
    *   `agents/`: AI Agent logic (CrewAI, Ollama, Groq).
    *   `utils/`: Helper scripts.
*   `database/`: Database schemas.

## 🚀 Getting Started

1.  **Navigate to the deployment folder:**
    ```bash
    cd deploy
    ```

2.  **Start the stack:**
    ```bash
    docker compose up -d
    ```

3.  **Access the services:**
    *   **Mission Control:** `http://localhost:8501`
    *   **Portainer:** `http://localhost:9000`
    *   **Grafana:** `http://localhost:3000`
    *   **n8n:** `http://localhost:5678`

## 🛠️ Development

Install dependencies locally:
```bash
pip install -r requirements.txt
```
