"""
To learn how to call Google AI Models using LangChain, you can use the following code snippet.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-3.6-flash",
    temperatue = 1.5,
    max_tokens = 100
    )

result = model.invoke("Write a paragraph about India.")

print(result.content[0]['text'])
# print(type(result))