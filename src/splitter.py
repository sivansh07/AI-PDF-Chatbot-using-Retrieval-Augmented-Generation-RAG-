from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,  #Each chunk will contain approximately 1000 characters.
        chunk_overlap=200  #The last 200 characters of one chunk will also appear at the beginning of the next chunk.
    )

    chunks = text_splitter.split_documents(documents)

    return chunks