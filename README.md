# 🚀 FastAPI API with OpenAI Agents SDK

## 📌 Description
This API is a **PoC (Proof of Concept)** demonstrating the integration of **OpenAI's Agents SDK** with **FastAPI**. It enables:
- 💬 **Interact with OpenAI** (`/chat/`) – General chat-based interactions with OpenAI's GPT-4o
- 📄 **Analyze a PDF file** (`/analyze-pdf/`) – Extract and summarize text from uploaded PDFs
- ❓ **Ask Questions About PDFs** (`/ask-pdf/`) – Upload a PDF and ask specific questions about its content
- 🗄️ **Store queries in an SQLite/PostgreSQL database** for retrieval

---

## ⚡ Installation

### 1️⃣ **Clone the project**
```bash
git clone https://github.com/kooljo/poc-agent-sdk.git
cd poc-agent-sdk
```

### 2️⃣ **Create a virtual environment and install dependencies**
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 3️⃣ **Configure environment variables**
Create a `.env` file and add your OpenAI key:
```ini
OPENAI_API_KEY="your_openai_key"
```

### 4️⃣ **Start the API**
```bash
uvicorn main:app --reload
```

The API is accessible at:
👉 `http://127.0.0.1:8000`
👉 Swagger Documentation: `http://127.0.0.1:8000/docs`

---

## 📌 Usage

### 🔹 **1. Ask OpenAI a question** (`/chat/`)
```bash
curl -X 'POST' 'http://127.0.0.1:8000/chat/' \
-H 'Content-Type: application/json' \
-d '{"prompt": "Explain FastAPI to me"}'
```

### 🔹 **2. Analyze a PDF file** (`/analyze-pdf/`)
```bash
curl -X 'POST' 'http://127.0.0.1:8000/analyze-pdf/' -F 'file=@document.pdf'
```

### 🔹 **3. Ask a question about an uploaded PDF** (`/ask-pdf/`)
```bash
curl -X 'POST' 'http://127.0.0.1:8000/ask-pdf/' -F 'file=@document.pdf' -F 'question=What is the main topic of this document?'
```

### 🔹 **4. View query history** (`/history/`)
```bash
curl -X 'GET' 'http://127.0.0.1:8000/history/'
```

---

## 🔧 Tech Stack
- **FastAPI** 🚀 – High-performance API framework
- **OpenAI Agents SDK** 🤖 – AI-powered assistant with file search
- **PostgreSQL / SQLite** 🗄️ – Database for storing queries

---

## 📌 Future Improvements 🚀
✅ Add support for PostgreSQL
✅ Integrate JWT authentication
✅ Deploy to a cloud server (Railway, Vercel, AWS...)
✅ Improve large PDF handling with text chunking

💡 **Ideas and suggestions are welcome!**

📌 **Author:** Jean-Noé KOLLO | 💼 [Linkedin](https://www.linkedin.com/in/jnkollo/) | 🐙 [GitHub](https://github.com/kooljo)
