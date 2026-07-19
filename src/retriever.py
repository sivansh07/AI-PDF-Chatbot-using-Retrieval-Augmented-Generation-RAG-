from langchain_core.vectorstores import VectorStoreRetriever

def get_retriever(vector_store):
    retriever = vector_store.as_retriever(
    search_type="similarity",  #Use semantic similarity search.
    search_kwargs={"k": 4}   #Returns top 4 Most Similar Chunks
    )
    return retriever

