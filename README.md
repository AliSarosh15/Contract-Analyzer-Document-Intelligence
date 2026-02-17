# 🚀 Contract Analyzer & Document Intelligence

An AI-powered backend system that extracts, analyzes, and summarizes contract documents using OCR and Large Language Models (Mistral & DeepSeek).
This project processes PDFs and images, extracts text using OCR and document parsing tools, and sends the extracted content to LLMs for summarization and
risk analysis — helping users understand important or risky clauses before agreeing to contracts.

---
## 🧠 Core Capabilities

- 📂 Accepts contract documents (PDF, Images, Text)
- 🔍 Extracts text using:
  - PyMuPDF (PDF parsing)
  - PyTesseract (OCR for images)
- 🤖 Integrates with LLMs:
  - Mistral
  - DeepSeek
  (via OpenRouter API)
- 📌 Generates:
  - Concise contract summary
  - Highlighted risky clauses
  - Important obligations users should review
- 🗄️ Stores processed data in PostgreSQL
- 🧩 Modular Flask Blueprint architecture
- 📡 RESTful API design

---
## 🛠️ Tech Stack

- Python
- Flask
- PostgreSQL
- SQLAlchemy
- PyTesseract
- PyMuPDF
- OpenRouter API
- Mistral LLM
- DeepSeek LLM
- REST Architecture

---
## 📂 Project Structure

```
Contract-Analyzer-Document-Intelligence/
│
├── app/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── config.py
│   ├── extensions.py
│   │
│   ├── my_uploads/
│   │   ├── terms-and-conditions-template.pdf
│   │   ├── termsandconditionsample.jpg
│   │   └── vox-terms-and-conditions-example.pdf
│   │
│   ├── TandC/
│   │   ├── __pycache__/
│   │   ├── model/
│   │   │   ├── __pycache__/
│   │   │   └── TCmodel.py
│   │   │
│   │   ├── routes/
│   │   │   ├── __pycache__/
│   │   │   └── TCroutes.py
│   │   │
│   │   ├── schema/
│   │   │   ├── schemas.py
│   │   │   └── __init__.py
│   │   │
│   │   └── utils.py
│   │
│   ├── tcenv/
│   │   ├── bin/
│   │   ├── include/
│   │   ├── lib/
│   │   ├── lib64/
│   │   └── pyvenv.cfg
│   │
│   └── User/
│       ├── __pycache__/
│       │
│       ├── models/
│       │   ├── __pycache__/
│       │   └── user_model.py
│       │
│       ├── routes/
│       │   ├── __pycache__/
│       │   └── user_routes.py
│       │
│       ├── schemas/
│       │   ├── schemas.py
│       │   └── __init__.py
│       │
│       └── utils.py
│
├── .gitignore
├── requirements.txt
└── run.py
```

---
## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/AliSarosh15/Contract-Analyzer-Document-Intelligence.git
cd Contract-Analyzer-Document-Intelligence
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv tcenv
```

Activate it:

**Mac/Linux**
```bash
source tcenv/bin/activate
```

**Windows**
```bash
tcenv\Scripts\activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Setup PostgreSQL

Create database:

```sql
CREATE DATABASE contract_analyzer_db;
```

Update `config.py`:

```python
SQLALCHEMY_DATABASE_URI = "postgresql://username:password@localhost:5432/contract_analyzer_db"
```

---

### 5️⃣ Configure OpenRouter API Key

Mac/Linux:
```bash
export OPENROUTER_API_KEY=your_api_key
```

Windows:
```bash
set OPENROUTER_API_KEY=your_api_key
```

---

### 6️⃣ Run the Application

```bash
python run.py
```

Server runs at:

```
http://127.0.0.1:5000/
```

---

## 🔄 Application Workflow

1. User uploads contract document (PDF/Image/Text)
2. System extracts raw text:
   - PyMuPDF for PDFs
   - PyTesseract for images
3. Extracted content is sent to:
   - Mistral LLM
   - DeepSeek LLM
4. LLM returns:
   - Structured summary
   - Risky clauses
   - Important highlights
5. Results are stored in PostgreSQL

---

## 🎯 What This Project Demonstrates

- OCR integration in backend systems
- LLM API integration
- Prompt engineering
- RESTful API design
- Modular Flask architecture
- Database modeling with SQLAlchemy
- Real-world AI document intelligence pipeline

---

## 🚀 Future Enhancements

- JWT Authentication
- Role-based access control
- Swagger / OpenAPI documentation
- Docker containerization
- Cloud deployment (Render / AWS)
- Background task processing (Celery)
- API rate limiting

---

## 👨‍💻 Author

**Ali Sarosh**  
Backend Developer | AI Integrations | REST APIs  

GitHub: https://github.com/AliSarosh15  
LinkedIn: https://www.linkedin.com/in/ali-sarosh-332b90280  

---

## 📜 License

This project is developed for educational and demonstration purposes.
