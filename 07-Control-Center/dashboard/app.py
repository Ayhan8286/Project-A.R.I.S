import streamlit as st

st.set_page_config(
    page_title="Mission Control",
    page_icon="🚀",
    layout="wide",
)

st.title("🚀 Mission Control")

st.markdown("""
Welcome to the Mission Control dashboard. Here you can monitor your AI agents,
infrastructure, and local intelligence services.
""")

st.header("System Status")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="n8n Workflow Engine", value="Online", delta="Port 5678")

with col2:
    st.metric(label="Portainer", value="Online", delta="Port 9000")

with col3:
    st.metric(label="Local Brain (Ollama)", value="Online", delta="Port 11434")

st.subheader("Quick Links")
st.markdown("""
*   [n8n Workflow Editor](http://localhost:5678)
*   [Portainer Management](http://localhost:9000)
*   [Airflow Orchestrator](http://localhost:8080)
""")
