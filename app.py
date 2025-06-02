import streamlit as st
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI
import os
import tempfile

# Get OpenAI key from secrets or environment
openai_api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")

st.title("📚 Alumni LBS Chatbot")

# Upload PDFs
uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    with st.spinner("Processing PDFs..."):
        all_docs = []
        
        for uploaded_file in uploaded_files:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(uploaded_file.read())
                tmp_file_path = tmp_file.name

            st.success(f"✅ Uploaded: {uploaded_file.name}")
            loader = PyMuPDFLoader(tmp_file_path)
            docs = loader.load()
            all_docs.extend(docs)
            os.unlink(tmp_file_path)

        # Split into chunks
        splitter = CharacterTextSplitter(chunk_size=400, chunk_overlap=80)
        chunks = splitter.split_documents(all_docs)

        # Embed
        embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        vectordb = FAISS.from_documents(chunks, embedding=embeddings)
        retriever = vectordb.as_retriever(search_kwargs={"k": 6})

        # LLM + QA
        llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=openai_api_key, temperature=0)
        qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, chain_type="stuff")

        st.session_state.qa = qa
        st.success("📚 Documents processed successfully!")

# Ask questions
if hasattr(st.session_state, 'qa'):
    st.subheader("Ask your question:")
    query = st.text_input("Your question here")
    if query:
        with st.spinner("Thinking..."):
            result = st.session_state.qa.run(query)
            st.write("🤖 Answer:", result)
else:
    st.info("Please upload PDF files to start asking questions.")

