from dotenv import load_dotenv
from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from pydantic import BaseModel
import openai
from openai import OpenAI
from openai import AssistantEventHandler
from fastapi import FastAPI, UploadFile, File, HTTPException
import os
import pdfplumber
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()

# Initialize FastAPI app
app = FastAPI(title="A quick FastAPI to test OpenAI SDK agent")

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Database setup (SQLite)
DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Table to store chat history
class QueryHistory(Base):
    __tablename__ = "queries"
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String)
    response = Column(String)

Base.metadata.create_all(bind=engine)

# Pydantic model for handling chat input
class Question(BaseModel):
    prompt: str

# Create Assistants for PDF Analysis and Q&A
assistantAnalyzePdf = client.beta.assistants.create(
    name="PDF Analyzer Agent",
    instructions="You are an assistant that summarizes PDF documents.",
    tools=[{"type": "code_interpreter"}, {"type": "file_search"}],  # ✅ Uses file_search for document analysis
    model="gpt-4o"
)

assistantAskPdf = client.beta.assistants.create(
    name="PDF Q&A Agent",
    instructions="You are an assistant that answers questions based on uploaded PDFs.",
    tools=[{"type": "file_search"}],  # Enables file-based search
    model="gpt-4o"
)

# Route to analyze a PDF and generate a summary using an assistant
@app.post("/analyze-pdf/")
async def analyze_pdf_with_agent(file: UploadFile = File(...)):
    try:
        # Extract text from the uploaded PDF
        with pdfplumber.open(file.file) as pdf:
            text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])

        # Create a conversation thread for the assistant
        thread = client.beta.threads.create()
        
        # Send the extracted text to the assistant for summarization
        client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=f"Summarize this document:\n\n{text[:5000]}"  # Limit to first 5000 characters
        )

        # Execute the assistant's task and retrieve the response
        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=assistantAnalyzePdf.id
        )

        # Retrieve the summary response
        messages = client.beta.threads.messages.list(thread_id=thread.id)

        if messages.data:
            summary = messages.data[0].content[0].text.value
            return {"summary": summary}
        else:
            return {"error": "No response from the assistant"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Route to chat with OpenAI
@app.post("/chat/")
def ask_openai(question: Question):
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": question.prompt}]
        )
        result = response.choices[0].message.content

        # Store chat history in database
        db = SessionLocal()
        db.add(QueryHistory(question=question.prompt, response=result))
        db.commit()

        return {"response": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Route to upload and summarize a PDF using OpenAI ChatCompletion
@app.post("/upload-pdf/")
async def analyze_pdf(file: UploadFile = File(...)):
    try:
        with pdfplumber.open(file.file) as pdf:
            text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
        
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an assistant that summarizes documents."},
                {"role": "user", "content": f"Summarize this document:\n\n{text[:4000]}"}  # Limit to 4000 characters
            ]
        )
        summary = response.choices[0].message.content

        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Route to ask a question about an uploaded PDF
@app.post("/ask-pdf/")
async def ask_pdf(file: UploadFile = File(...), question: str = Form(...)):
    try:
        # Upload the file to OpenAI
        file_bytes = file.file.read()
        uploaded_file = client.files.create(
            file=(file.filename, file_bytes), purpose="assistants"
        )

        # Create a conversation thread
        thread = client.beta.threads.create()

        # Attach the file to the assistant with correct tool usage
        client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=f"Answer this question based on the uploaded document:\n\n{question}",
            attachments=[{"file_id": uploaded_file.id, "tools": [{"type": "file_search"}]}]  # ✅ Corrected format
        )

        # Start the assistant's response process
        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=assistantAskPdf.id
        )

        # Retrieve the assistant's answer
        messages = client.beta.threads.messages.list(thread_id=thread.id)

        if messages.data:
            answer = messages.data[0].content[0].text.value
            return {"question": question, "answer": answer}
        else:
            return {"error": "No response from the assistant"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Route to retrieve stored chat history
@app.get("/history/")
def get_query_history():
    db = SessionLocal()
    history = db.query(QueryHistory).all()
    return {"history": [{"question": q.question, "response": q.response} for q in history]}
