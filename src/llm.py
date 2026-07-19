import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

os.getenv("GOOGLE_API_KEY")

load_dotenv()


def get_llm():
    llm = ChatGoogleGenerativeAI(
        model="gemini-flash-latest",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0.3
    )

    return llm