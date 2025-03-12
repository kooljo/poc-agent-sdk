# FastAPI API with OpenAI Agents SDK

## Description
This project is a **FastAPI**-based API that integrates OpenAI's **Agents SDK** to analyze and interact with PDF documents. It allows you to:

- 💬 **Chat with OpenAI** (`/chat/`)
- 📄 **Analyze a PDF file** and get a summary (`/analyze-pdf/`)
- ❓ **Ask questions about a PDF** (`/ask-pdf/`)
- 🗄️ **Store queries in an SQLite database**

## Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/kooljo/poc-agent-sdk.git
cd poc-agent-sdk
```

### 2️⃣ Create a virtual environment and install dependencies
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 3️⃣ Configure environment variables
Create a `.env` file and add your OpenAI API key:
```ini
OPENAI_API_KEY="your_openai_key"
```

### 4️⃣ Start the API
```bash
uvicorn main:app --reload
```
The API is accessible at:
- **Swagger Documentation**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc Documentation**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Endpoints

### 🔹 1. Chat with OpenAI (`/chat/`)
```bash
curl -X 'POST' 'http://127.0.0.1:8000/chat/' \
-H 'Content-Type: application/json' \
-d '{"prompt": "Explain FastAPI to me"}'
```

### 🔹 2. Analyze a PDF (`/analyze-pdf/`)
```bash
curl -X 'POST' 'http://127.0.0.1:8000/analyze-pdf/' -F 'file=@cv.pdf'
```

### 🔹 3. Ask a question about a PDF (`/ask-pdf/`)
```bash
curl -X 'POST' 'http://127.0.0.1:8000/ask-pdf/' -F 'file=@cv.pdf' -F 'question=What is this document about?'
```

### 🔹 4. View chat history (`/history/`)
```bash
curl -X 'GET' 'http://127.0.0.1:8000/history/'
```


## Future Improvements 🚀
✅ Add support for PostgreSQL
✅ Implement authentication with JWT
✅ Deploy to a cloud service (AWS, Railway, Vercel...)

📌 **Author:** Jean-Noé KOLLO | [LinkedIn](https://www.linkedin.com/in/jnkollo/) | [GitHub](https://github.com/kooljo)
