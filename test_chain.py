from src.loader import load_pdf
from src.splitter import split_documents
from src.vector_store import create_vector_store
from src.retriever import get_retriever
from src.chain import get_rag_chain

# Load PDF
documents = load_pdf("pdfs/C++_Book.pdf")

# Split
chunks = split_documents(documents)

# Vector Store
vector_store = create_vector_store(chunks)

# Retriever
retriever = get_retriever(vector_store)

# RAG Chain
rag_chain = get_rag_chain(retriever)

# Ask Question
response = rag_chain.invoke(
    {
        "input": "What is Inheritance in C++?"
    }
)

print(response["answer"])