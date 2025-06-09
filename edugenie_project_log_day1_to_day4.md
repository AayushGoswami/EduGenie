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

---

## 🗓️ Day 3: Streamlit Chatbot UI Integration and Modularization
**🎯 Objective:** Build a modular, chat-style Streamlit UI for EduGenie and refactor logic into reusable components.

### ✅ Tasks Completed:

1. **Planned Chat UI Design:**
   - Decided to use Streamlit with a chatbot-style layout.
   - Goal was to make the app more user-friendly and scalable.

2. **Verified Repo Structure:**
   - Confirmed that we are adhering to the previously decided architecture (from reference image).

3. **Prototype Streamlit UI Created:**
   - Built initial version of `streamlit_app.py` with basic chat input and single-turn response rendering.

4. **Resolved `st.experimental_rerun` Error:**
   - Encountered deprecation error with `st.experimental_rerun()`.
   - Removed it and simplified rerun logic based on chat input.

5. **Identified Remaining Files:**
   - Discussed the purpose of files like `utils.py`, `config.yaml`, `test_pipeline.py`, and `ingest_content.py`.

6. **Built `utils.py`:**
   - Moved reusable UI and logic into `utils.py`.
   - Functions include chat history management, context formatting, answer display, and message container.

7. **Refactored `streamlit_app.py`:**
   - Replaced inline logic with function calls from `utils.py`.
   - Imports updated and code modularized for better readability.

8. **Fixed Import Error (`app.utils`):**
   - Faced `ModuleNotFoundError` due to incorrect import path.
   - Corrected it to `from utils import ...` and ensured correct `sys.path` setup.

9. **Handled `NoneType` Context Error:**
   - Issue: Chatbot was trying to iterate over `None` context chunks.
   - Solution: Added a check before looping through context to prevent runtime error.

10. **Set App Branding and Context:**
    - Updated app title to: `EduGenie - Your NCERT Science AI Assistant`.
    - Confirmed that the app’s theme is focused on UPSC aspirants using Class 7–10 NCERT Science books.

### ✅ Outcome:
- 🟢 Chatbot UI is functional and modular.
- 🟢 Full end-to-end QA with conversation memory now possible.
- 🟢 Error handling and formatting improved.
- 🟢 Ready for ingestion enhancements and deployment features next.

---

## 🗓️ Day 4: Knowledge Base Expansion and System Validation
**🎯 Objective:** Expand EduGenie's RAG system to include NCERT Class 11 & 12 Science books and verify end-to-end functionality.

---

### ✅ Tasks Completed

1. **Expanded Dataset with New PDFs**
   - Added Class 11 & 12 PDFs: Biology, Chemistry, Physics (both volumes)
   - Files stored in `data/raw/`
   - Filenames like `physics_class_12_1.pdf`, `biology_class_11.pdf`, etc.

2. **Ingestion Automation Script Built**
   - Created `scripts/ingest_content.py`
   - Automatically processes all PDFs in `data/raw/`
   - Uses `semantic_chunker.py`, `embedder.py`, `vector_store.py` internally

3. **Successful Ingestion of Full Dataset**
   - Ran the script and embedded all chunks from Class 7–12 Science PDFs
   - Updated and saved the FAISS index

4. **Tested Retrieval & Generation**
   - Used `test_generator.py` with advanced UPSC-style queries
   - Confirmed: Chunks retrieved from higher class files (e.g., Class 12 Chemistry)
   - Answers generated via Groq (LLaMA 3) were relevant and context-aware

5. **Evaluation Metrics Discussion (Postponed)**
   - Discussed ROUGE, BERTScore, BLEU for evaluating QA accuracy
   - Decided to implement automated evaluation later

6. **Reviewed Remaining Project Components**
   - Identified outstanding features and modules like:
     - `config.yaml` for parameter tuning
     - Subject-wise filtering
     - File upload interface
     - Quiz/Flashcard/Study Plan generation (optional add-ons)

---

## ✅ Final Status (End of Day 4)

- 🟢 Full NCERT Science corpus from Class 7 to 12 ingested
- 🟢 Working RAG pipeline with expanded knowledge base
- 🟢 Functional chatbot UI with Groq integration
- 🟢 Project architecture still modular and clean
- 🔧 Ready to implement config, quiz features, file upload, or deploy

---

## 🔜 Next Steps

- Build `config.yaml` to externalize model and DB parameters
- Enable subject/class filtering during retrieval
- Add file upload & auto-ingestion from Streamlit UI
- Implement `test_pipeline.py` for batch QA testing
- Optionally: Add quiz/flashcard/study plan generation modules
- Prepare app for deployment (Streamlit Cloud or HuggingFace Spaces)

