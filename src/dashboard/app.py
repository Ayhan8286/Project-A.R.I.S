import streamlit as st
from langchain_community.llms import Ollama
import time

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

st.divider()

st.header("🤖 Local Brain Interface")

# Initialize Local Brain Connection
try:
    # Using the container name 'gtm_ollama' as specified
    llm = Ollama(base_url="http://gtm_ollama:11434", model="llama3")
    st.success("Connected to Local Brain (Ollama)")
except Exception as e:
    st.error(f"Failed to connect to Local Brain: {e}")

prompt = st.text_area("Enter a prompt for the Local Brain:", "Why is running LLMs locally important?")

if st.button("Start Agent"):
    if prompt:
        with st.spinner("Agent is thinking..."):
            try:
                # Basic error handling and feedback
                start_time = time.time()
                response = llm.invoke(prompt)
                end_time = time.time()

                st.markdown("### Agent Response")
                st.write(response)
                st.caption(f"Response generated in {end_time - start_time:.2f} seconds.")

            except Exception as e:
                st.error(f"An error occurred during execution: {e}")
    else:
        st.warning("Please enter a prompt first.")
