# Generate sentence embeddings
# edugenie/embeddings/embedder.py

from sentence_transformers import SentenceTransformer
import json
from pathlib import Path
from typing import List, Dict

class Embedder:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        return self.model.encode(texts, show_progress_bar=True, convert_to_numpy=True).tolist()

    def load_chunks(self, processed_dir: str) -> List[Dict]:
        all_chunks = []
        for file in Path(processed_dir).glob("*.jsonl"):
            with open(file, "r", encoding="utf-8") as f:
                for line in f:
                    chunk = json.loads(line)
                    all_chunks.append(chunk)
        return all_chunks

    def embed_chunks(self, processed_dir: str) -> List[Dict]:
        chunks = self.load_chunks(processed_dir)
        texts = [chunk["content"] for chunk in chunks]
        embeddings = self.embed_texts(texts)

        for i, emb in enumerate(embeddings):
            chunks[i]["embedding"] = emb

        return chunks
