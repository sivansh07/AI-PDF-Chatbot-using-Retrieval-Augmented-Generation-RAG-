from src.llm import get_llm

llm = get_llm()

response = llm.invoke("What is C++?")

print(response.content)


# from google import genai
# import os
# from dotenv import load_dotenv

# load_dotenv()

# client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# for model in client.models.list():
#     print(model.name)
