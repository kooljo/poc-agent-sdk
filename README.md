# 🚀 FastAPI API with OpenAI and Web Search

## 📌 Description
This API allows you to:
- 💬 **Interact with OpenAI** (`/chat/`)
- 📄 **Analyze a PDF file** and get a summary (`/analyze-pdf/`)
- 🗄️ **Store queries in an SQLite database**

---

## ⚡ Installation

### 1️⃣ **Clone the project**
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
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

### 🔹 **3. View query history** (`/history/`)
```bash
curl -X 'GET' 'http://127.0.0.1:8000/history/'
```

---

## 🐳 Deployment with Docker

### 1️⃣ **Build and run the container**
```bash
docker-compose up --build -d
```

### 2️⃣ **Stop the API**
```bash
docker-compose down
```

---

## 📌 Future Improvements 🚀
✅ Add support for PostgreSQL
✅ Integrate JWT authentication
✅ Deploy to a cloud server (Railway, Vercel, AWS...)

💡 **Ideas and suggestions are welcome!**

📌 **Author:** Jean-Noé KOLLO | 💼 [Linkedin](https://www.linkedin.com/in/jnkollo/) | 🐙 [GitHub](https://github.com/kooljo)
