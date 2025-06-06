# utils.py
# UI/data helpers
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st
import yaml
from rag.retriever import Retriever
from rag.generator import generate_answer

def initialize_chat_history():
    """Initialize chat history in session state if not already present."""
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

def format_context_chunk(ctx):
    """Format a retrieved context chunk for display."""
    return f"**`{ctx['source']}` | 🧩 Chunk {ctx['chunk_id']}`**\n\n> {ctx['content'][:500]}..."

def show_chat_interface():
    chat_container = st.container()

    """Display the chat interface with input and history."""
    with chat_container:
        for message in st.session_state.chat_history:
            message_container(message['role'], message['content'])

    user_input = st.chat_input(placeholder="Ask a question...")

    if user_input:
        # Append user input to chat history
        st.session_state.chat_history.append(
            {"role": "user", "content": user_input}
            )
        message_container("user", user_input)
        # Clear the input box
        # st.session_state.chat_input = ""

        # Retrieve relevant information
        top_chunks = []
        answer = ""
        # Show loading spinner while retrieving and generating
        with st.spinner("🔍 Retrieving relevant information..."):
            retriever = Retriever(top_k=5)
            top_chunks = retriever.retrieve(user_input)

        if top_chunks:
            with st.spinner("🧠 Generating answer with LLaMA 3 via Groq..."):
                answer = generate_answer(top_chunks, st.session_state.chat_history, user_input)
        else:
            answer = "No relevant information found in the provided documents."
        # Append answer to chat history
        st.session_state.chat_history.append(
            {"role": "assistant", "content": answer}
        )
        # Display the answer
        message_container("assistant", answer, top_chunks)

def message_container(role, content, top_chunks=None):
    """Display a message in the chat interface."""
    if role == "user":
        with st.container():
            st.markdown(
                    f"""
                    <div style="display: flex; justify-content: flex-end; margin: 1rem 0;">
                        <div style="background-color: #034f01; padding: 0.75rem; border-radius: 15px; max-width: 80%;">
                            <p style="margin: 0; color: #ededed;">🧑‍🎓 {content}</p>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            # st.markdown(f"**🧑‍🎓 You:** {content}")
    else:
        with st.container():
            st.markdown(
                    f"""
                    <div style="display: flex; justify-content: flex-start; margin: 1rem 0;">
                        <div style="background-color: #021617; padding: 0.75rem; border-radius: 15px; max-width: 80%;">
                            <p style="margin: 0;"><strong>🤖 EduGenie</strong><br>{content}</p>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            # st.markdown(f"**🤖 EduGenie:** {content}")
            if top_chunks:
                with st.expander("📄 Retrieved Context", expanded=False):
                    for j, ctx in enumerate(top_chunks, 1):
                        st.markdown(f"**{j}.** {format_context_chunk(ctx)}")
                    st.markdown("---")

def load_config(path: str = "config/config.yaml"):
    """Load YAML configuration file."""
    with open(path, "r") as f:
        return yaml.safe_load(f)
