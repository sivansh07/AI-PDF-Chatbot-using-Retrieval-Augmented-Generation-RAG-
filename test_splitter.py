from src.loader import load_pdf
from src.splitter import split_documents

pdf_path = "pdfs/C++_Book.pdf"   # or "pdfs/C++_Book.pdf"

documents = load_pdf(pdf_path)

chunks = split_documents(documents)

print(f"Total Pages   : {len(documents)}")
print(f"Total Chunks  : {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0].page_content)

print("\nSecond Chunk:\n")
print(chunks[1].page_content)

print("\nMetadata:")
print(chunks[0].metadata)


# Total Characters in PDF ÷ Effective Chunk Length ≈ Number of Chunks
# My Project contains
#1,500,000 ÷ 800 ≈ 1875 chunks

