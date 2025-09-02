# Community RAG Chatbot in Streamlit with FAISS

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://rag-chatbot-hvdsf3j3jxe7c8m3mk3blu.streamlit.app/)

Upload your documents and get cited answers. The app chunks, embeds, and indexes your files locally in FAISS.  
Originally built as a two-week MVP for **LBS Alumni Career Services** to test coverage and speed at scale.

---

## 🚀 Try it online

**Live demo:**  
👉 [rag-chatbot-hvdsf3j3jxe7c8m3mk3blu.streamlit.app](https://rag-chatbot-hvdsf3j3jxe7c8m3mk3blu.streamlit.app/)

**How to test**
1. Click the link above.  
2. Upload a **PDF, TXT, or Markdown** file.  
3. Ask a question such as:  
   - “How do I book a coaching session?”  
   - “What are the eligibility rules for job board access?”  
4. Review the answer with citations. Use *Reset index* to try different docs.

---

## ⚡ Quickstart locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
streamlit run app.py
Environment variables (set in .env or your terminal):

ini
Copiar código
OPENAI_API_KEY=sk-...
EMBEDDING_MODEL=text-embedding-3-small
LLM_MODEL=gpt-4o-mini
VECTOR_INDEX_PATH=.cache/faiss_index
📚 What it does
Upload PDF, TXT, or Markdown documents

Automatic chunking → embeddings → FAISS index (stored locally)

Ask questions and get answers with citations from your own docs

⚙️ How it works
mermaid
Copiar código
flowchart LR
  U[Upload files] --> S[Split into chunks]
  S --> E[Embeddings]
  E --> V[FAISS index]
  Q[User query] --> EQ[Embed query]
  EQ --> R[Top-k search]
  R --> G[LLM answer with citations]
  V <---> R
Chunking
Strategy: sliding window

Chunk size: 1000 characters

Overlap: 200 characters

Why: preserves policy/FAQ context while keeping embedding cost low

Retrieval
FAISS IndexFlatIP with L2-normalized 1536-d embeddings

Top-k = 5

Minimum score = 0.25

Answering: gpt-4o-mini with temperature 0.2

Answers only from context; otherwise responds “unknown”

📊 Results from the MVP demo
First pass produced about 70–80% good answers on high-priority topics and highlighted gaps in Job Board access, FinTech events, and CV guidance.

🛣 Roadmap
See docs/ROADMAP.md for short-, mid-, and long-term steps.

🔒 Privacy (MVP)
See docs/PRIVACY.md.
No external persistence by default. For basic usage metrics, Cloudflare Web Analytics (cookie-free) is suggested.

📑 Case study
See docs/CASE_STUDY.md for context, approach, and outcomes.

📜 License
MIT License — see LICENSE.

pgsql
Copiar código

👉 You can copy all of that directly into your `README.md`.  

Do you also want me to prepare a **shorter “executive README”** version that fits in one screen (good for recruiters/community), with details only in `/docs`?
