# semantic_chunker.py

import os
import json
import fitz  # PyMuPDF
import nltk
from nltk.tokenize import sent_tokenize
from pathlib import Path

# Download punkt tokenizer model (only needed once)
# nltk.download()

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text()
    return text

def semantic_chunk(text, chunk_size=300):
    sentences = sent_tokenize(text)
    chunks = []
    current_chunk = []
    current_length = 0

    for sent in sentences:
        words = sent.split()
        if current_length + len(words) > chunk_size:
            chunks.append(" ".join(current_chunk))
            current_chunk = []
            current_length = 0
        current_chunk.append(sent)
        current_length += len(words)

    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks

def process_all_pdfs(input_dir, output_dir, chunk_size=300):
    os.makedirs(output_dir, exist_ok=True)

    for pdf_file in Path(input_dir).glob("*.pdf"):
        text = extract_text_from_pdf(pdf_file)
        chunks = semantic_chunk(text, chunk_size)

        data = [{"source": pdf_file.name, "chunk_id": i, "content": chunk}
                for i, chunk in enumerate(chunks)]

        out_file = Path(output_dir) / f"{pdf_file.stem}.jsonl"
        with open(out_file, "w", encoding="utf-8") as f:
            for entry in data:
                f.write(json.dumps(entry) + "\n")

        print(f"✅ Processed: {pdf_file.name} → {out_file.name}")

if __name__ == "__main__":
    process_all_pdfs("data/raw", "data/processed", chunk_size=300)
