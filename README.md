# Community RAG Chatbot in Streamlit with FAISS

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://rag-chatbot-hvdsf3j3jxe7c8m3mk3blu.streamlit.app/)

Upload your documents and get cited answers. The app chunks, embeds and indexes your files locally in FAISS.  
Originally built as a two-week MVP for LBS Alumni Career Services to test coverage and speed at scale.

## Try it online

Live demo  
https://rag-chatbot-hvdsf3j3jxe7c8m3mk3blu.streamlit.app/

How to test  
1. Click the link above.  
2. Upload a PDF or TXT or Markdown file.  
3. Ask a question such as How do I book a coaching session or What are the eligibility rules for job board access.  
4. Review the answer with citations. Use Reset index to try different docs.

## Quickstart locally

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
streamlit run app.py

OPENAI_API_KEY=sk-...
EMBEDDING_MODEL=text-embedding-3-small
LLM_MODEL=gpt-4o-mini
VECTOR_INDEX_PATH=.cache/faiss_index


## What it does

• Upload PDF or TXT or MD
• Automatic chunking then embeddings then FAISS index stored locally
• Ask questions and get citations from your own docs

## How it works
flowchart LR
  U[Upload files] --> S[Split into chunks]
  S --> E[Embeddings]
  E --> V[FAISS index]
  Q[User query] --> EQ[Embed query]
  EQ --> R[Top k search]
  R --> G[LLM answer with citations]
  V <---> R


#Chunking which is explicit
• Strategy is sliding window
• Chunk size is 1000 characters
• Overlap is 200 characters
• Reason is to keep policy and FAQ context intact while keeping cost low

#Retrieval
• FAISS IndexFlatIP with L2 normalized 1536 dimensional embeddings
• Top k equals 5
• Minimum score equals 0.25
• Generation uses gpt-4o-mini with temperature 0.2 and answers only from context or says unknown

#Results from the MVP demo

First pass produced about 70 to 80 percent good answers on high priority topics and highlighted gaps in Job Board access, FinTech events and CV guidance.

#Roadmap

See docs or open docs and read ROADMAP.md for short, mid and long term steps.

#Privacy for the MVP

See docs or open docs and read PRIVACY.md. No external persistence by default. For basic usage metrics use Cloudflare Web Analytics.

#Case study

See docs or open docs and read CASE_STUDY.md for context, approach and outcomes.





