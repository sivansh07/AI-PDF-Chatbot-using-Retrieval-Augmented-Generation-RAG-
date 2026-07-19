from src.loader import load_pdf
from src.splitter import split_documents
from src.vector_store import create_vector_store
from src.retriever import get_retriever

pdf_path = "pdfs/C++_Book.pdf"   # or "pdfs/C++_Book.pdf"

documents = load_pdf(pdf_path)
chunks = split_documents(documents)

vector_store = create_vector_store(chunks)

retriever = get_retriever(vector_store)

results = retriever.invoke("What is inheritance?")

print(f"Retrieved {len(results)} chunks")

print("\nFirst Result:\n")
print(results[0].page_content)

print("\nMetadata:")
print(results[0].metadata)