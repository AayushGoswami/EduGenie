# EduGenie

An end-to-end Retrieval-Augmented Generation (RAG) pipeline for educational content.

## Structure

- `data/`: Raw and processed data
- `scripts/`: Data ingestion and testing scripts
- `chunking/`: Text chunking logic
- `embeddings/`: Embedding generation and vector store
- `rag/`: Retriever and generator modules
- `app/`: User-facing app (Streamlit or FastAPI)
- `config/`: Configuration files
- `docs/`: Documentation and diagrams

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure `.env` and `config/config.yaml` as needed.
3. Run the app:
   ```bash
   streamlit run app/streamlit_app.py
   ```
