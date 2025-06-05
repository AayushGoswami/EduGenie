# vector_store.py
# Interact with pgvector or FAISS
# embeddings/vector_store.py

import os
import json
import faiss
import numpy as np
from typing import List, Dict

class FAISSVectorStore:
    def __init__(self, index_path: str = "embeddings/faiss_index.index", metadata_path: str = "embeddings/metadata.jsonl"):
        self.index_path = index_path
        self.metadata_path = metadata_path
        self.index = None
        self.metadata = []

    def build_index(self, embedded_chunks: List[Dict]):
        print("🔧 Building FAISS index...")

        # Extract embeddings and convert to numpy array
        vectors = np.array([chunk["embedding"] for chunk in embedded_chunks]).astype("float32")
        self.metadata = [ {k: v for k, v in chunk.items() if k != "embedding"} for chunk in embedded_chunks ]

        dim = vectors.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(vectors)

        # Save index and metadata
        faiss.write_index(self.index, self.index_path)
        with open(self.metadata_path, "w") as f:
            for item in self.metadata:
                f.write(json.dumps(item) + "\n")

        print(f"✅ Saved FAISS index with {len(self.metadata)} entries.")

    def load_index(self):
        if not os.path.exists(self.index_path) or not os.path.exists(self.metadata_path):
            raise FileNotFoundError("❌ FAISS index or metadata file not found. Please build the index first.")

        print("📥 Loading FAISS index and metadata...")
        self.index = faiss.read_index(self.index_path)
        self.metadata = []
        with open(self.metadata_path, "r") as f:
            for line in f:
                self.metadata.append(json.loads(line))

    def search(self, query_vector: List[float], top_k: int = 5) -> List[Dict]:
        if self.index is None:
            raise ValueError("❌ FAISS index not loaded.")

        query_np = np.array([query_vector]).astype("float32")
        distances, indices = self.index.search(query_np, top_k)

        results = []
        for idx in indices[0]:
            if idx < len(self.metadata):
                results.append(self.metadata[idx])
        return results
