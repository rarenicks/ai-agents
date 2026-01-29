import streamlit as st
from src.agents.assistant import get_assistant
import uuid

st.set_page_config(page_title="Agno Agent Blueprint", page_icon="🤖")

st.title("Agno Production Agent 🤖")
st.markdown("This interface demonstrates a production-ready Agno agent with persistence and tool calling.")

# Initialize session state for chat history and session ID
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get response from agent
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # Initialize agent with current session ID
            agent = get_assistant(session_id=st.session_state.session_id)
            
            # Run agent and stream response
            response_stream = agent.run(prompt, stream=True)
            
            for chunk in response_stream:
                # Agno stream chunks might be objects or strings. 
                # Adjust based on Agno's actual stream output.
                # Assuming chunk.content or chunk exists.
                content = chunk.content if hasattr(chunk, 'content') else str(chunk)
                if content:
                    full_response += content
                    message_placeholder.markdown(full_response + "▌")
            
            message_placeholder.markdown(full_response)
        except Exception as e:
            st.error(f"Error: {e}")
            full_response = "Sorry, I encountered an error."

    # Add assistant message to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})

# Sidebar for session info
with st.sidebar:
    st.header("Session Info")
    st.write(f"**Session ID:** `{st.session_state.session_id}`")
    if st.button("New Session"):
        st.session_state.session_id = str(uuid.uuid4())
        st.session_state.messages = []
        st.rerun()
