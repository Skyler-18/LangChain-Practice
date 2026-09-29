"""
Now the types of messages are implemented in the chatbot. The chatbot uses SystemMessage, HumanMessage and AIMessage to maintain the history of the conversation.
The chatbot runs in a loop, taking user input and generating responses until the user types "exit" to terminate the conversation. 
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv 

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-3.6-flash",
    temperature = 1.5
    )

chat_history = [
    SystemMessage(content="You are a helpful AI assistant.")
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content[0]["text"]))

    print("AI: ", result.content[0]["text"])

print("---------------------------")
print(chat_history)