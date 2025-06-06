# # streamlit_app.py
# # User-facing web app
# import sys
# from pathlib import Path
# sys.path.append(str(Path(__file__).resolve().parent.parent))

# import streamlit as st
# from rag.retriever import Retriever
# from rag.generator import generate_answer

# # Initialize retriever
# retriever = Retriever(top_k=3)

# # App UI
# st.set_page_config(page_title="EduGenie - Ask Your Book AI", layout="wide")
# st.title("📘 EduGenie: Ask Your Science Book")
# st.markdown("""
# Welcome to **EduGenie**! Ask any question based on your Science textbooks from Class 7 to 10,
# and get AI-generated, context-grounded answers from your books.
# """)

# # User question input
# question = st.text_input("❓ Enter your question:", placeholder="e.g. How does photosynthesis work in plants?")

# # Submit button
# if st.button("🔍 Get Answer") and question:
#     with st.spinner("📥 Retrieving relevant content..."):
#         top_chunks = retriever.retrieve(question)

#     st.subheader("🔍 Retrieved Chunks:")
#     for i, chunk in enumerate(top_chunks, 1):
#         st.markdown(f"**{i}.** *{chunk['source']} | Chunk {chunk['chunk_id']}*\n\n> {chunk['content'][:300]}...")

#     with st.spinner("🧠 Generating answer with LLaMA 3 via Groq..."):
#         answer = generate_answer(top_chunks, question)

#     st.success("✅ Answer Generated:")
#     st.markdown(f"""
#     <div style='background-color: #f0f2f6; padding: 1em; border-radius: 10px;'>
#         <b>Answer:</b><br>{answer}
#     </div>
#     """, unsafe_allow_html=True)

# # Footer
# st.markdown("""
# ---
# Made with ❤️ using Streamlit, FAISS, and LLaMA 3 via Groq.
# """)
