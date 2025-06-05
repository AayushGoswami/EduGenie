# scripts/test_retriever.py

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from rag.retriever import Retriever

def main():
    retriever = Retriever(top_k=3)
    query = "How do plants prepare their food?"
    results = retriever.retrieve(query)

    print("\n🔍 Retrieved Chunks:")
    for r in results:
        print(f"- [{r['source']}][Chunk {r['chunk_id']}] → {r['content'][:150]}...\n")

if __name__ == "__main__":
    main()
