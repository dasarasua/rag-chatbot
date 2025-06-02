import streamlit as st
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from langchain_community.chat_models import ChatOpenAI
import os
import numpy as np
openai_api_key = st.secrets["OPENAI_API_KEY"]
if "OPENAI_API_KEY" in st.secrets:
    openai_api_key = st.secrets["OPENAI_API_KEY"]
else:
    load_dotenv()
    openai_api_key = os.getenv("OPENAI_API_KEY")

st.title("📚 Alumni LBS Chatbot (Local PDF Upload)")

# Upload PDF
uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    os.makedirs("data", exist_ok=True)
    all_docs = []

    for uploaded_file in uploaded_files:
        file_path = os.path.join("data", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.read())
        st.success(f"✅ Uploaded: {uploaded_file.name}")

        loader = PyMuPDFLoader(file_path)
        docs = loader.load()
        all_docs.extend(docs)


    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(all_docs)


    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma.from_documents(chunks, embedding=embeddings)
    retriever = vectordb.as_retriever(search_kwargs={"k": 5})

    # Load LLM (CHATGOPT)
    llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    openai_api_key=openai_api_key,
    temperature=0)

    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="map_reduce")

    st.subheader("Ask your question:")
    query = st.text_input("Your question here")

    if query:
        result = qa.run(query)
        st.write("🤖 Answer:", result)
