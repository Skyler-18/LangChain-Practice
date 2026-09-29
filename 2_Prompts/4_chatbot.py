"""
This is a simple chatbot that uses Google Gemini 3.6 model to generate responses based on user input. The chatbot runs in a loop, taking user input and generating responses until the user types "exit" to terminate the conversation.
It is to understand the need of maintaining history while talking to a chatbot using API.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-3.6-flash",
    temperature = 1.5
    )

while True:
    user_input = input("You: ")

    if user_input == "exit":
        break

    result = model.invoke(user_input)
    print("AI: ", result.content[0]["text"])