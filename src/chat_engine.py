import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()

# Gemini Model
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)


# Embedding Model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load Vector Database
db = FAISS.load_local(
    "vectorstore",
    embedding_model,
    allow_dangerous_deserialization=True
)

def retrieve_context(question):

    docs = db.similarity_search(
        question,
        k=4
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    return context

def ask(question):

    context = retrieve_context(question)

    prompt = f"""
        You are Chaitanya AI Career Assistant.

        Your job is to answer questions about Chaitanya Rastogi.

        Rules:

        1. Use only provided context.
        2. Be professional.
        3. Be concise.
        4. If information is missing say:

        'I don't have that information in Chaitanya's profile.'

        5. If asked:
        'Tell me about Chaitanya'

        generate a short professional summary.

        Context:
        {context}

        Question:
        {question}
    """

    response = llm.invoke(prompt)

    return response.content

def mock_interview(user_message):

    prompt = f"""
        You are a professional technical interviewer.

        You are interviewing Chaitanya Rastogi.

        Focus on:
        - Python
        - SQL
        - Data Science
        - Machine Learning
        - Generative AI

        User Message:
        {user_message}

        If the user says:
        'start interview'

        then ask the first interview question.

        Otherwise continue the interview naturally.
        """

    response = llm.invoke(prompt)

    return response.content