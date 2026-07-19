from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import (
    create_stuff_documents_chain,
)

from src.llm import get_llm
from src.prompt import RAG_PROMPT


def get_rag_chain(retriever):
    llm = get_llm()

    document_chain = create_stuff_documents_chain(
        llm=llm,
        prompt=RAG_PROMPT,
    )

    rag_chain = create_retrieval_chain(
        retriever,
        document_chain,
    )

    return rag_chain