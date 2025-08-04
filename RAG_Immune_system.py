import os
import fitz
import chromadb
from nomic import login, embed
from langchain.text_splitter import RecursiveCharacterTextSplitter
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import UserMessage, SystemMessage
from azure.core.credentials import AzureKeyCredential
from dotenv import load_dotenv
from collections import deque
from prompt import prompts

# Initialize only once
def initialize_system():
    load_dotenv()  
    login(os.getenv("NOMIC_API_KEY"))  
    
    chroma_client = chromadb.PersistentClient(path="./chroma_db")
    collection = chroma_client.get_or_create_collection("immune_docs")
    
    chat_client = ChatCompletionsClient(
        endpoint="https://models.github.ai/inference",
        credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
    )
    
    return collection, chat_client

collection, chat_client = initialize_system()
conversation_memory = deque(maxlen=7)

def answer_question(question):
    # Embed the question
    q_emb = embed.text(
        texts=[question],
        model="nomic-embed-text-v1.5"
    )["embeddings"][0]

    results = collection.query(query_embeddings=[q_emb], n_results=5)
    docs = [doc for sublist in results["documents"] for doc in sublist]
    context = "\n\n".join(docs)


    history_text = ""
    for past_q, past_a in conversation_memory:
        history_text += f"Previous Question: {past_q}\nPrevious Answer: {past_a}\n\n"

    # Send to GPT 
    prompt = prompts.format( history_text=history_text,
        context=context,
        question=question
    )

    messages = [SystemMessage("You are a helpful medical assistant.")]
    for past_q, past_a in conversation_memory:
        messages.append(UserMessage(past_q))
        messages.append(SystemMessage(past_a))
    messages.append(UserMessage(prompt))

    response = chat_client.complete(
        messages=messages,
        model="gpt-4o-mini"
    ).choices[0].message["content"]
    

    conversation_memory.append((question, response))

    return str(response)

# Only run initialization if executed directly
if __name__ == "__main__":
    # For testing the function directly
    print(answer_question("What is lupus?"))


