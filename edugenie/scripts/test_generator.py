# edugenie/scripts/test_generator.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rag.generator import generate_answer
from rag.retriever import Retriever

def main():
    print("📥 Loading vector index and metadata...")
    retriever = Retriever(top_k=3)

    # Sample question (you can change this)
    question = "What is chlorophyll?"

    print(f"❓ Question: {question}")
    
    # Get top relevant chunks using the retriever
    top_chunks = retriever.retrieve(question)
    # print(top_chunks)
    print("\n🔍 Retrieved Context Chunks:")
    for i, chunk in enumerate(top_chunks, 1):
        print(f"{i}. 📄 {chunk['source']} | 🧩 Chunk {chunk['chunk_id']}")
        print(f"   📚 {chunk['content'][:200]}...\n")
        # print(f"{i}. {chunk['content'][:200]}...\n")  # Show preview

    # Generate answer using Groq + LLaMA 3
    print("🧠 Generating Answer from LLaMA 3...")
    answer = generate_answer(top_chunks, question)

    print("\n✅ Final Answer:\n")
    print(answer)

if __name__ == "__main__":
    main()
