import streamlit as st
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
import os
load_dotenv()
print("KEY:", os.getenv("OPENAI_API_KEY"))
print("🔑 KEY FOUND:", os.getenv("OPENAI_API_KEY"))
openai_api_key = os.getenv("OPENAI_API_KEY")

st.title("📚 RAG Chatbot (Local PDF Upload)")

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
