from src.loader import load_pdf
from src.splitter import split_documents
from src.vector_store import create_vector_store

pdf_path = "pdfs/C++_Book.pdf"   # or "pdfs/C++_Book.pdf"

documents = load_pdf(pdf_path)
chunks = split_documents(documents)

vector_store = create_vector_store(chunks)

print("Vector Store Created Successfully!")

print(type(vector_store))
