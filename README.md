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

## 📊 Monitoring (Mission Control)

The **Mission Control Cockpit** is available at `http://localhost:8501`.

*   **System Status:** Real-time uptime checks for n8n, Qdrant, and Ollama.
*   **Audit Logs:** View the `ai_logs` table from Postgres directly in the UI.
*   **Chat:** Interact directly with the local Llama 3 model for quick queries.

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

## 🧠 The Brain (Knowledge Base)

The GTM Engine uses **Qdrant** as its long-term memory. You can feed text data into the brain to train your agents.

### Training the Brain
1.  Add text files to `src/brain_data/`.
2.  Run the ingestion script:
    ```bash
    python src/utils/ingest.py
    ```
    *This will load, split, embed, and store your data in Qdrant.*

### Testing the Brain
To verify the AI can retrieve this information:
```bash
python src/utils/test_brain.py
```

---

## ⚡ The Synapse (Gateway Service)

The **Gateway Service** acts as the neural bridge between the outside world (like n8n) and the Vector Brain.

*   **URL:** `http://localhost:5000`
*   **Purpose:** Receives HTTP requests, vectorizes them, and queries Qdrant.
*   **Endpoint:** `POST /search`
    ```json
    { "query": "What is V-List?" }
    ```

---

## 🤖 The Autonomous Agent (Workflow)

The **V-List Agent v1** is an n8n workflow that automates the "Lead -> RAG -> Writer -> DB" pipeline.

### How it Works
1.  **Lead Input:** Receives lead data (Company, Name, Pain Point).
2.  **RAG (Retrieval):** Asks the **Gateway Service** (`gtm_gateway:5000`) for relevant solutions from the Brain.
3.  **Writer:** Uses **Ollama** (`gtm_ollama:11434`) to draft a hyper-personalized cold email using the retrieved context.
4.  **Audit Trail:** Logs the action and result to the `ai_logs` table in **Postgres**.
5.  **First Contact:** Sends the email via **SMTP** (supports Gmail, Outlook, etc.).

### SMTP Configuration
To enable email delivery, you must configure your SMTP credentials in n8n:
1.  Go to n8n Credentials.
2.  Create a new "SMTP" credential.
3.  For Gmail: Use `smtp.gmail.com`, port `465` (SSL/TLS), User: `your@gmail.com`, Password: `YOUR_APP_PASSWORD`.

### Using the Workflow
1.  Open n8n at `http://localhost:5678`.
2.  Import the workflow file located at: `src/workflows/v1_agent.json`.
3.  Execute the workflow to see the agent in action.

---

## ❓ Troubleshooting

Run into issues? Check the **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** file for detailed solutions to common problems like port conflicts or Docker errors.
