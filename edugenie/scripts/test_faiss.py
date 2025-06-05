# scripts/test_faiss.py

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from embeddings.embedder import Embedder
from embeddings.vector_store import FAISSVectorStore

def main():
    processed_dir = "data/processed"
    embedder = Embedder()
    vector_store = FAISSVectorStore()

    # Load and embed chunks
    print("🧠 Embedding chunks...")
    chunks = embedder.embed_chunks(processed_dir)

    # Build and save FAISS index
    vector_store.build_index(chunks)

    # Load index back and search
    vector_store.load_index()
    query = "What is photosynthesis?"
    query_vector = embedder.embed_texts(query)
    results = vector_store.search(query_vector, top_k=3)

    print("\n🔍 Top Results:")
    for r in results:
        print(f"- [{r['source']}][Chunk {r['chunk_id']}] → {r['content'][:120]}...\n")

if __name__ == "__main__":
    main()

