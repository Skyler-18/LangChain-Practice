"""
This file demonstrates how to use the PydanticOutputParser to ensure the AI model returns data in a specific structured format defined by a Pydantic model. The PydanticOutputParser allows you to define a schema for the expected output using Pydantic, making it easier to validate and work with the returned data.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-3.6-flash",
    temperatue = 1.5
    )

class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(description="Age of the person")
    city: str = Field(description="Name of the city the person belongs to")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template = 'Give me the name, age, city of a fictional {place} person \n{format_instruction}',
    input_variables = ['place'],
    partial_variables = {'format_instruction': parser.get_format_instructions() }
)

# prompt = template.invoke({'place': 'India'})
# print(prompt) ##We can check how the prompt looks like after formatting instructions are added to it

chain = template | model | parser

result = chain.invoke({'place': 'India'})

print(result)