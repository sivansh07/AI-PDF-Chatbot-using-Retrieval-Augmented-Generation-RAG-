from src.loader import load_pdf

pdf_path = "pdfs/C++_Book.pdf"

documents = load_pdf(pdf_path)

print(f"Total Pages: {len(documents)}")

print("\nFirst Page:\n")
print(documents[0].page_content[:500])

print("\nMetadata:")
print(documents[0].metadata)