# scripts/test_embedder.py

import sys
from pathlib import Path

# ✅ Add the root directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from embeddings.embedder import Embedder

def main():
    processed_dir = "data/processed"
    embedder = Embedder()

    print("🔄 Embedding chunks...")
    embedded_chunks = embedder.embed_chunks(processed_dir)

    print(f"✅ Total chunks embedded: {len(embedded_chunks)}")
    print("🧾 Sample chunk:")
    print(embedded_chunks[0])  # show first embedded chunk

if __name__ == "__main__":
    main()
