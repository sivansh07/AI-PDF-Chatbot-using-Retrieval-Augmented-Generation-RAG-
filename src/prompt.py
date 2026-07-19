from langchain_core.prompts import ChatPromptTemplate


RAG_PROMPT = ChatPromptTemplate.from_template(
    """
You are an AI assistant that answers questions ONLY from the provided context.

Rules:
1. Use only the provided context.
2. If the answer is not present in the context, reply:
   "I couldn't find that information in the uploaded PDF."
3. Do not make up or assume information.
4. Keep your answers clear and concise.

Context:
{context}

Question:
{input}
"""
)