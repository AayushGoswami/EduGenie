# retriever.py
# Vector search interface
# rag/retriever.py

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from embeddings.embedder import Embedder
from embeddings.vector_store import FAISSVectorStore

class Retriever:
    def __init__(self, top_k: int = 5):
        self.embedder = Embedder()
        self.vector_store = FAISSVectorStore()
        self.top_k = top_k
        self.vector_store.load_index()

    def retrieve(self, query: str):
        query_vector = self.embedder.embed_texts(query)
        top_chunks = self.vector_store.search(query_vector, top_k=self.top_k)
        return top_chunks
