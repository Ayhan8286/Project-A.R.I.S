# 🚀 GTM Engine: Ultimate AI Stack

Welcome to the **GTM (Go-To-Market) Engine**. This is a production-ready, local-first stack for building AI agents, automating workflows, and orchestrating data.

## 🌟 Features

*   **Local Brain:** Run Llama 3 locally using **Ollama**.
*   **Workflow Automation:** **n8n** for visual workflow orchestration.
*   **Mission Control:** Custom **Streamlit** dashboard to manage agents.
*   **Vector Memory:** **Qdrant** for long-term AI memory.
*   **Observability:** **Prometheus** & **Grafana** for monitoring.
*   **Infrastructure:** Complete **Docker Compose** stack.

---

## 🏁 Getting Started (Baby Steps)

Follow these simple steps to get your engine running.

### 1. Prerequisites
Ensure you have the following installed:
*   [Docker Desktop](https://www.docker.com/products/docker-desktop/) (and make sure it's running!)
*   [Python 3.9+](https://www.python.org/downloads/)
*   [Git](https://git-scm.com/)

### 2. Setup
Clone the repository and run the setup script. This will prepare your environment and install dependencies.

```bash
git clone <your-repo-url>
cd gtm-engine
./setup.sh
```

### 3. Configure Credentials
The setup script created a `.env` file for you. Open it and add your keys:

```bash
# Open .env in your favorite editor
nano .env
```
*   **Required:** Add your `GROQ_API_KEY` if you plan to use cloud agents.
*   **Optional:** Change database passwords if deploying to production.

### 4. Launch the Engine 🚀
Start the entire stack with one command:

```bash
./start.sh
```
*Wait a few minutes for all images to download and start.*

---

## 🖥️ Accessing the System

Once running, you can access the following services in your browser:

| Service | URL | Description |
| :--- | :--- | :--- |
| **Mission Control** | [http://localhost:8501](http://localhost:8501) | Main UI for AI Agents |
| **n8n** | [http://localhost:5678](http://localhost:5678) | Workflow Automation Editor |
| **Portainer** | [http://localhost:9000](http://localhost:9000) | Docker Container Management |
| **Grafana** | [http://localhost:3000](http://localhost:3000) | System Monitoring (User: `admin`, Pass: `admin`) |

---

## 🛠️ How to Develop

### Repository Structure
*   `src/`: This is where your code lives.
    *   `src/agents/`: Python code for your AI agents (`crewai`, etc.).
    *   `src/dashboard/`: The Streamlit dashboard code (`app.py`).
*   `deploy/`: Docker configuration files.
*   `terraform/`: Cloud infrastructure code (optional).

### Editing the Dashboard
1.  Open `src/dashboard/app.py`.
2.  Make changes to the Python code.
3.  Refresh [http://localhost:8501](http://localhost:8501) to see changes instantly.

### Adding New Dependencies
1.  Add the package name to `requirements.txt`.
2.  Run `./setup.sh` again.
3.  If it's for the Docker container, you may need to rebuild:
    ```bash
    cd deploy
    docker compose up -d --build
    ```

---

## ❓ Troubleshooting

Run into issues? Check the **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** file for detailed solutions to common problems like port conflicts or Docker errors.
