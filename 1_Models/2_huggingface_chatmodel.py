"""
To learn how to call HuggingFace AI Models using LangChain, you can use the following code snippet.
"""

from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id = "meta-llama/Llama-3.1-8B-Instruct",
    task = "text-generation",
    temperature = 0.7,
    max_new_tokens = 200
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("Write a paragraph about India.")

print(result.content)