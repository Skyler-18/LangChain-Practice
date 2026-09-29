"""
This file demonstrates how to use structured output with Pydantic models to ensure the AI model returns data in a specific format.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from dotenv import load_dotenv 
from pydantic import BaseModel, Field
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = "gemini-3.6-flash",
    temperature = 1.5
    )

#schema
class Review(BaseModel):
    key_themes: list[str] = Field(description="A list of key themes or topics mentioned in the review")
    summary: str = Field(description="A brief summary of the review")
    sentiment: Literal["pos", "neg"] = Field(description="The sentiment of the review (positive/negative/neutral)")
    pros: Optional[list[str]] = Field(default=None, description="A list of positive aspects or advantages mentioned in the review")
    cons: Optional[list[str]] = Field(default=None, description="A list of negative aspects or disadvantages mentioned in the review")
    name: Optional[str] = Field(default=None, description="The name of the reviewer, if mentioned in the review")

structured_model = model.with_structured_output(Review)

result = structured_model.invoke('''
I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it's an absolute powerhouse! The Snapdragon 8 Gen 3
processor makes everything lightning fast-whether I'm gaming, multitasking, or editing photos. The 5000mAh battery easily
lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me
away is the 200MP camera-the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x
actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung's One UI still comes with
bloatware-why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard
pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful

Cons:
Bulky and heavy-not great for one-handed use
Bloatware still exists in One UI
Expensive compared to competitors

Review by Hardik
''')

print(result)
print(type(result))
print(result.summary)
print(result.sentiment)
print(result.key_themes)
print(result.pros)
print(result.cons)
print(result.name)