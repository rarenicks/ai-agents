import streamlit as st
import requests
import uuid
import time

# Page Config
st.set_page_config(page_title="Google AI Agent System", page_icon="🤖", layout="wide")

# API URL
BASE_URL = "http://localhost:8000"

# Header
st.title("🤖 Google AI Agent System Core")
st.markdown("Powered by **Gemini Flash**, **LangGraph**, and **Vertex AI**.")

# Session State for Chat History
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())
    st.session_state.messages = []

# Sidebar for controls
with st.sidebar:
    st.header("⚙️ Controls")
    if st.button("New Session"):
        st.session_state.session_id = str(uuid.uuid4())
        st.session_state.messages = []
        st.rerun()  # Rerun the app to reflect changes
    
    st.markdown("---")
    st.markdown(f"**Session ID:** `{st.session_state.session_id}`")
    
    status_placeholder = st.empty()
    try:
        r = requests.get(f"{BASE_URL}/health")
        if r.status_code == 200:
            status_placeholder.success("Engine Online")
        else:
            status_placeholder.error("Engine Offline")
    except:
        status_placeholder.error("Engine Connection Failed")

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Ask me anything... (try 'Search for recent AI news')"):
    # Add user message to state
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Call API
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        with st.spinner("Thinking..."):
            try:
                payload = {
                    "session_id": st.session_state.session_id,
                    "message": prompt
                }
                response = requests.post(f"{BASE_URL}/agent/chat", json=payload)
                if response.status_code == 200:
                    data = response.json()
                    full_response = data["response"]
                    message_placeholder.markdown(full_response)
                else:
                    message_placeholder.error(f"Error: {response.status_code} - {response.text}")
            except Exception as e:
                message_placeholder.error(f"Connection Error: {e}")
                
    # Add assistant response to state
    if full_response:
        st.session_state.messages.append({"role": "assistant", "content": full_response})
