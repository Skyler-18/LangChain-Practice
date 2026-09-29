"""
This file demonstrates a simple 3 step chain.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-3.6-flash",
    temperature = 1.5
    )

prompt = PromptTemplate(
    template = 'Write a brief note on {topic}',
    input_variables = ['topic']
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic': 'Cricket'})

print(result)
chain.get_graph().print_ascii()  #This is how we can visualize the chain in a tree format. It is very useful when we have complex chains with multiple branches and we want to understand the flow of data through the chain.