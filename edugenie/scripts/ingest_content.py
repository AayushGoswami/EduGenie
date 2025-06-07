# ingest_content.py
# Extract, preprocess, and chunk data

# scripts/ingest_content.py
import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from chunking.semantic_chunker import process_all_pdfs
from embeddings.embedder import Embedder
from embeddings.vector_store import FAISSVectorStore

RAW_DATA_DIR = "data/raw"
PROCESSED_DIR = "data/processed"


def ingest_all():
    embedder = Embedder()
    vector_store = FAISSVectorStore()

    print("\n📄 Processing all PDFs in data/raw ...")
    process_all_pdfs(RAW_DATA_DIR, PROCESSED_DIR)

    print(f"\n🧠 Embedding chunks from {PROCESSED_DIR} ...")
    embedded_chunks = embedder.embed_chunks(PROCESSED_DIR)

    print("\n💾 Saving to FAISS index ...")
    vector_store.build_index(embedded_chunks)
    print("✅ Ingestion Complete.")


if __name__ == "__main__":
    ingest_all()
