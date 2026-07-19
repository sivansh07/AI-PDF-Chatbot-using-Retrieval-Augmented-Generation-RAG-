import tempfile
import streamlit as st

from src.loader import load_pdf
from src.splitter import split_documents
from src.vector_store import create_vector_store
from src.retriever import get_retriever
from src.chain import get_rag_chain


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI PDF Chatbot",
    page_icon="📄",
    layout="wide"
)


# --------------------------------------------------
# Session State
# --------------------------------------------------

if "rag_chain" not in st.session_state:
    st.session_state.rag_chain = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# --------------------------------------------------
# Title
# --------------------------------------------------

st.title("📄 AI PDF Chatbot using RAG")

st.markdown(
    """
Ask questions from your uploaded PDF using
**Retrieval-Augmented Generation (RAG)**.
"""
)


# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.header("📂 Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"]
    )

    process_button = st.button("🚀 Process PDF")

    if process_button:

        if uploaded_file is None:
            st.warning("Please upload a PDF first.")

        else:

            with st.spinner("Processing PDF..."):

                # Save uploaded PDF temporarily
                with tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".pdf"
                ) as temp_file:

                    temp_file.write(uploaded_file.getbuffer())

                    pdf_path = temp_file.name

                # Pipeline
                documents = load_pdf(pdf_path)

                chunks = split_documents(documents)

                vector_store = create_vector_store(chunks)

                retriever = get_retriever(vector_store)

                rag_chain = get_rag_chain(retriever)

                # Store in Session State
                st.session_state.rag_chain = rag_chain

            st.success("✅ PDF processed successfully!")


# --------------------------------------------------
# Chat Interface
# --------------------------------------------------

question = st.chat_input(
    "Ask a question from your PDF..."
)

if question:

    if st.session_state.rag_chain is None:

        st.warning("Please upload and process a PDF first.")

    else:

        with st.spinner("Thinking..."):

            response = st.session_state.rag_chain.invoke(
                {
                    "input": question
                }
            )

            answer = response["answer"]

        # Save Chat
        st.session_state.chat_history.append(
            {
                "question": question,
                "answer": answer
            }
        )


# --------------------------------------------------
# Display Chat History
# --------------------------------------------------

for chat in st.session_state.chat_history:

    with st.chat_message("user"):
        st.write(chat["question"])

    with st.chat_message("assistant"):
        st.write(chat["answer"])

