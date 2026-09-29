"""
This file demonstrates the different types of messages that can be used when interacting with the AI models. It shows how to create and use SystemMessage, AIMessage, and HumanMessage objects.
This is a better approach than using simple lists as it helps us better understand which was the messages sent by user and which was the messages sent by AI. The messages are stored in a list called `messages`. The `messages` list is passed to the model's `invoke` method to generate responses based on the entire conversation history.
"""

from langchain_core.messages import SystemMessage, AIMessage, HumanMessage 
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-3.6-flash",
    temperature = 1.5
    )

messages = [
    SystemMessage(content="You are a helpful assistant.")
]

user_input = "Tell me about LangChain"
messages.append(HumanMessage(content=user_input))

result = model.invoke(messages)
messages.append(AIMessage(content=result.content[0]["text"]))

print(result.content[0]["text"])

print("=================================================")
print(messages)