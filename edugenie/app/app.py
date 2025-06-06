import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import streamlit as st
from utils import initialize_chat_history, show_chat_interface


# Page Configuration
st.set_page_config(page_title="EduGenie", page_icon=":books:", layout="centered", initial_sidebar_state="expanded")
st.title("📚 EduGenie - Your NCERT Science Chatbot")
st.caption("Focused on UPSC preparation using NCERT Class 7–10 Science content 📘")

initialize_chat_history()  # Ensure chat history is initialized

# Display the chat interface
show_chat_interface()

# Footer
st.markdown("""
---
Made with ❤️ using Streamlit, FAISS, and LLaMA 3 via Groq.
""")
# This code initializes a simple Streamlit app that allows users to ask questions
# based on their documents, retrieves relevant chunks using a retriever,
# and generates answers using a language model. The UI is designed to be user-friendly
# and informative, providing clear feedback during the retrieval and generation processes.
# The footer includes a note about the technologies used to build the app.
# This code is a complete Streamlit app that allows users to ask questions
# and get answers based on their documents, leveraging a retriever and a language model.
# The app is designed to be intuitive and responsive, providing a smooth user experience.
# The code is structured to handle user input, retrieve relevant information,
# and generate answers, all while maintaining a clean and informative UI.
# The app is built using Streamlit, a popular framework for creating web applications in Python.