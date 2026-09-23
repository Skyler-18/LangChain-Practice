"""
To learn how to use HuggingFace Embeddings with LangChain, you can use the following code snippet.
"""

from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
)

documents = ["Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.", 
             "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
              "Sachin Tendulkar, also known as 'God of Cricket', holds many batting records.", 
              "Rohit Sharma is known for his elegant batting and record-breaking double centuries.", 
              "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."]

vector = embedding.embed_documents(documents)

print(str(vector))