from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv 
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-3.6-flash",
    temperatue = 1.5
    )

#1st Prompt -> Detailed Report
template1 = PromptTemplate(
    template = 'Write a detailed report on {topic}',
    input_variables = ['topic']
)

#2nd Prompt -> Summary
template2 = PromptTemplate(
    template = 'Write a 5 line summary on the following text: /n {text}',
    input_variables = ['text']
)

prompt1 = template1.invoke({'topic': 'Black hole'})

result1 = model.invoke(prompt1)

prompt2 = template2.invoke({'text': result1})

result2 = model.invoke(prompt2) 

print(result1.content[0]['text'])
print(result2.content[0]['text'])