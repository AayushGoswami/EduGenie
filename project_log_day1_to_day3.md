# 📘 EduGenie: Project Development Log (Chronological)

---

## 🗓️ Day 1: Project Setup, Raw Data, and Initial Chunking
**🎯 Objective:** Set up the foundational structure, collect source material, and preprocess data.

### ✅ Tasks Completed:
1. **Project Structure Initialized:**
   - Created directories: `data/raw`, `data/processed`, `scripts/`, `embeddings/`, `rag/`, etc.

2. **Downloaded NCERT PDFs:**
   - Stored: `science_class_7.pdf` to `science_class_10.pdf` in `data/raw`.

3. **Semantic Chunking Implemented:**
   - Wrote `semantic_chunker.py` to tokenize and structure content using NLTK.

4. **NLTK Tokenizer Issue:**
   - **Issue:** `LookupError: Resource punkt not found.`
   - **Fix:** Used `nltk.download()` to open the downloader UI and install all needed packages.

5. **Broken PDF File Issue:**
   - **Issue:** `MuPDF error: zlib error: incorrect header check` (Class 8).
   - **Fix:** Replaced corrupted file with a working version.

### ✅ Outcome:
- 🟢 Project structure solidified.
- 🟢 All NCERT PDFs successfully parsed into structured chunks.

---

## 🗓️ Day 2: Embeddings, Retrieval, and Generation Pipeline
**🎯 Objective:** Build the complete RAG pipeline with embedding, retrieval, and answer generation.

### ✅ Embedding Stage:
- Created `embedder.py` using `sentence-transformers`.
- Created `vector_store.py` using FAISS to store vectors.
- Wrote `test_embedder.py`.

**Issues & Fixes:**
- **KeyError:** `chunk["text"]` → **Fix:** Used correct field `chunk["content"]`.
- **Module Import Error:** Fixed by appending project root to `sys.path`.

✅ Result: FAISS index built with 893 embedded chunks.

---

### ✅ Retrieval Stage:
- Developed `retriever.py` with `Retriever` class.
- Script `test_retriever.py` used to fetch top-k chunks for queries.

**Issue:** `retrieve_top_chunks` not recognized.  
**Fix:** Used method via instantiated class (`Retriever().retrieve()`).

✅ Result: Relevant chunks successfully retrieved for user queries.

---

### ✅ Generation Stage:
- Created `generator.py` to generate answers using **Groq API with LLaMA 3**.
- Wrote `test_generator.py`.

**Issues & Fixes:**
1. **Preview Error:** `KeyError` on printing chunk.  
   - **Fix:** Extracted `chunk["content"][:200]`.
2. **Join Error:** `TypeError: expected str, got dict`.  
   - **Fix:** Extracted just the `"content"` field before joining.
3. **Unstructured/Repetitive Answer:**  
   - **Fix:** Redesigned the prompt to guide the model in:
     - Structuring content.
     - Avoiding redundancy.
     - Maintaining semantic and chronological clarity.

✅ Result: Final output answers are now well-structured, coherent, and accurate.

---

## ✅ Current Status
- ✅ Working RAG pipeline from chunking ➝ embedding ➝ retrieval ➝ generation.
- ✅ Integrated with Groq (LLaMA 3).
- ✅ Tuned prompts improve output quality significantly.
- ✅ Tested with multiple questions and content sources.

---


## 🗓️ Day 3 – EduGenie RAG UI & Chatbot Integration

**🎯 Objective:** Design and implement a functional, interactive, and extensible Streamlit-based RAG chatbot UI for EduGenie, targeting UPSC aspirants using NCERT-based science content.

### 📌 Steps Taken & Progress Summary

| Step | Description | Objective | Issues Faced | Solution/Outcome |
|------|-------------|-----------|--------------|------------------|
| 1️⃣ | Planning Streamlit App UI | Build a chat-like interactive app for RAG-based Q&A | – | Decided to start from a prototype UI and scale gradually |
| 2️⃣ | Confirmed Repo Structure | Ensure the app follows the correct repo layout | Initially unsure of structure | Referred to repo diagram to realign |
| 3️⃣ | Prototype UI Created | Initial `streamlit_app.py` created with chat input and response generation | – | Functional base UI working with `Retriever` + `generate_answer()` |
| 4️⃣ | Deprecated API Issue | `streamlit.experimental_rerun()` caused error | Streamlit version removed it | Removed the line; app worked fine |
| 5️⃣ | Identified Missing Components | Listed out `utils.py`, `config.yaml`, `test_pipeline.py`, `ingest_content.py` | – | Created a clear plan for each |
| 6️⃣ | Built `utils.py` | Moved formatting and chat logic out of UI file | – | Functions modularized: display, formatting, appending |
| 7️⃣ | Refactored Streamlit App | Replaced logic with `utils.py` function calls | ImportError for `app.utils` | Fixed by importing as `from utils import ...` |
| 8️⃣ | Verified Full Chat Flow | Tested user Q&A flow end-to-end | – | Chat history and responses worked flawlessly |
| 9️⃣ | Runtime Warning (Torch) | `torch.classes` warning triggered by Streamlit reload | From internal watcher system | Ignored safely, no crash |
| 🔟 | Improved App Title | Wanted a UPSC-focused title | Explored options | Finalized: **EduGenie – Your NCERT Science AI Assistant** |

### 📦 Final Outcome

- ✅ Working chatbot UI (`streamlit.py`)
- ✅ Chat history retained across messages
- ✅ Answer and retrieved context formatted and shown
- ✅ UI logic moved to clean, reusable `utils.py`
- ✅ Title customized to reflect UPSC preparation context

### 🧠 Key Takeaways

- Chat interface now supports multi-turn Q&A
- Modular code is easier to scale and maintain
- UPSC-aligned branding is in place for user clarity

## 🔜 Next Steps
- Evaluate answers automatically using ROUGE/BLEU.
- Expand to additional subjects or regional languages.
- Deploy to Hugging Face or Streamlit Cloud.

---
