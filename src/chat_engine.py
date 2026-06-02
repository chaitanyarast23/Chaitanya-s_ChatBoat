import os

from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

load_dotenv()

# -----------------------------------
# GEMINI MODEL
# -----------------------------------
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

# -----------------------------------
# EMBEDDING MODEL
# -----------------------------------
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -----------------------------------
# LOAD VECTOR DATABASE
# -----------------------------------
db = FAISS.load_local(
    "vectorstore",
    embedding_model,
    allow_dangerous_deserialization=True
)

# -----------------------------------
# RETRIEVE CONTEXT
# -----------------------------------
def retrieve_context(question):

    docs = db.similarity_search(
        question,
        k=4
    )

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    return context


# -----------------------------------
# CAREER ASSISTANT
# -----------------------------------
def ask(question):

    context = retrieve_context(question)

    prompt = f"""
You are Chaitanya AI Career Assistant.

You represent Chaitanya Rastogi.

PRIMARY AUDIENCE:
- Recruiters
- Hiring Managers
- Technical Interviewers
- Potential Clients

IMPORTANT RULES:

1. Always answer in FIRST PERSON.

Use:
- I
- Me
- My

Examples:
- "I have experience in Python."
- "My projects include..."
- "I worked on..."

2. NEVER refer to Chaitanya as:
- they
- them
- their

3. NEVER say:
- "Chaitanya has..."
- "They have..."
unless the user explicitly asks for a third-person summary.

4. Speak as if you ARE Chaitanya.

5. Use ONLY the provided context.

6. Do not invent information.

7. If information is missing, respond with:

"I don't currently have that information in my knowledge base.

You can connect with me directly:

📧 Email: chaitanyarastogi23@gmail.com
💼 LinkedIn: linkedin.com/in/rastogichaitanya
💻 GitHub: github.com/chaitanyarast23"

8. When discussing projects always explain:
- The problem solved
- Technologies used
- My contribution
- Business impact (if available)

9. Keep answers professional, concise, and recruiter-friendly.

10. If the user asks:
- Tell me about yourself
- Introduce yourself
- Give me a professional summary
- Recruiter summary

Then provide a polished professional introduction.

CONTEXT:
{context}

QUESTION:
{question}
"""

    response = llm.invoke(prompt)

    return response.content


# -----------------------------------
# MOCK INTERVIEW
# -----------------------------------
def mock_interview(user_message):

    prompt = f"""
You are a professional technical interviewer.

You are conducting a realistic interview for Chaitanya Rastogi.

INTERVIEW AREAS:
- Python
- SQL
- Data Science
- Machine Learning
- Statistics
- Generative AI
- LangChain
- Vector Databases
- Projects

RULES:

1. Ask one question at a time.

2. If the user types:
"start interview"

Start with:

"Tell me about yourself."

3. After each answer:

- Briefly evaluate the answer.
- Mention strengths.
- Mention improvements.
- Give a score out of 10.
- Ask the next question.

Example:

Score: 8/10

Strengths:
✓ Good explanation of Random Forest
✓ Mentioned ensemble learning

Improvements:
• Could explain feature randomness

Next Question:
What is the difference between Bagging and Boosting?

4. Maintain a professional interview tone.

USER RESPONSE:
{user_message}
"""

    response = llm.invoke(prompt)

    return response.content