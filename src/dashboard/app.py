import streamlit as st
import pandas as pd
import psycopg2
import os
import requests
from langchain_community.llms import Ollama

# Configuration
DB_HOST = os.environ.get("POSTGRES_HOST", "postgres")
DB_NAME = os.environ.get("POSTGRES_DB", "n8n_db")
DB_USER = os.environ.get("POSTGRES_USER", "n8n")
DB_PASS = os.environ.get("POSTGRES_PASSWORD", "securepassword123")
N8N_WEBHOOK_URL = "http://n8n:5678/webhook/agent-trigger"

st.set_page_config(
    page_title="Mission Control v2.0",
    page_icon="🚀",
    layout="wide",
)

st.title("🚀 Mission Control v2.0")
st.markdown("Monitor your AI agents, infrastructure, and local intelligence services.")

# --- SIDEBAR: AGENT STARTER ---
with st.sidebar:
    st.header("⚡ Agent Starter (The Front Door)")
    with st.form("agent_form"):
        company_name = st.text_input("Company Name", "TechCorp")
        contact_name = st.text_input("Contact Name", "Sarah")
        contact_email = st.text_input("Contact Email", "sarah@example.com")
        pain_point = st.text_area("Pain Point", "spending too much on SDR salaries")

        submitted = st.form_submit_button("🚀 Launch Agent")

        if submitted:
            payload = {
                "company": company_name,
                "contact_name": contact_name,
                "contact_email": contact_email,
                "pain_point": pain_point
            }
            try:
                response = requests.post(N8N_WEBHOOK_URL, json=payload)
                if response.status_code == 200:
                    st.success("✅ Signal sent to Nervous System (n8n Webhook)!")
                else:
                    st.error(f"❌ Failed to trigger agent: {response.text}")
            except Exception as e:
                st.error(f"❌ Connection Error: {e}")

    st.markdown("---")
    st.header("🎮 Actions")
    if st.button("🔄 Refresh Data"):
        st.rerun()
    st.markdown("---")
    st.markdown("**Quick Links**")
    st.markdown("- [n8n Workflow](http://localhost:5678)")
    st.markdown("- [Portainer](http://localhost:9000)")
    st.markdown("- [Grafana](http://localhost:3000)")

# --- SYSTEM STATUS ---
st.header("📡 System Status")
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="n8n Engine", value="Online", delta="Port 5678")
with col2:
    st.metric(label="Vector Brain", value="Active", delta="Qdrant")
with col3:
    st.metric(label="Local LLM", value="Ready", delta="Llama 3")
with col4:
    st.metric(label="Database", value="Connected", delta="Postgres")

st.divider()

# --- DATABASE CONNECTION ---
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        return conn
    except Exception as e:
        st.error(f"Database Connection Failed: {e}")
        return None

# --- AI LOGS ---
st.header("📝 AI Agent Logs")
conn = get_db_connection()
if conn:
    try:
        # Fetch logs
        query = "SELECT id, agent_name, action_taken, result_summary, timestamp as created_at FROM ai_logs ORDER BY timestamp DESC LIMIT 20"
        df = pd.read_sql(query, conn)
        st.dataframe(df, use_container_width=True)
        conn.close()
    except Exception as e:
        st.error(f"Error fetching logs: {e}")
else:
    st.warning("Could not connect to database to fetch logs.")

st.divider()

# --- LOCAL BRAIN INTERFACE ---
st.header("🧠 Chat with Local Brain")
prompt = st.chat_input("Ask your local Llama 3 model...")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                llm = Ollama(base_url="http://gtm_ollama:11434", model="llama3")
                response = llm.invoke(prompt)
                st.write(response)
            except Exception as e:
                st.error(f"Error communicating with Ollama: {e}")
