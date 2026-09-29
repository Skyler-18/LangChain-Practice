"""
This file demonstrates how to use the StructuredOutputParser to ensure the AI model returns data in a specific structured format. The StructuredOutputParser allows you to define a schema for the expected output, making it easier to extract and work with the returned data.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_classic.output_parsers import ResponseSchema, StructuredOutputParser
## langchain-core is library which contains the core modules that are mostly used in langchain. It is a dependency of langchain-classic. That's why StructuredOutputParser is imported from langchain_classic.output_parsers instead of langchain_core.output_parsers.

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-3.6-flash",
    temperature = 1.5
    )

schema = [
    ResponseSchema(name='fact1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact3', description='Fact 3 about the topic'),
]

parser = StructuredOutputParser(response_schemas=schema)

template = PromptTemplate(
    template = 'Give 3 facts about the {topic} \n{format_instruction}',
    input_variables = ['topic'],
    partial_variables = {'format_instruction': parser.get_format_instructions() }
)

chain = template | model | parser

result = chain.invoke({'topic': 'Black hole'})

print(result)