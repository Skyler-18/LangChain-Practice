"""
This file demonstrates how to use the JsonOutputParser to ensure the AI model returns data in a specific JSON format.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-3.6-flash",
    temperature = 1.5
    )

parser = JsonOutputParser()

template = PromptTemplate(
    template = 'Give me the name, age, city of a fictional person \n{format_instruction}',
    input_variables = [],
    partial_variables = {'format_instruction': parser.get_format_instructions() }  #The information about the output format is passed to the prompt template as a partial variable
)

prompt = template.format()
# print(prompt) ##We can check how the prompt looks like after formatting instructions are added to it

##Normal code without using chains
# result = model.invoke(prompt)
# final_result = parser.parse(result.content[0]['text'])  #The output is parsed using the JsonOutputParser
# print(type(final_result))

##Using chains
chain = template | model | parser

result = chain.invoke({})  #We have to send dictionary even if we are not passing any input variables.

print(result)