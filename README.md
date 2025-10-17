# 🐍 HNG Stage 0 – Profile API

A simple **FastAPI** microservice that exposes a `/me` endpoint returning profile information, the current UTC timestamp, and a random cat fact (fetched from an external API).

---

🚀 Live Demo

> 🔗 **Deployed here:** https://hngstage0-production-5da8.up.railway.app/me 

---

## 📁 Project Structure

hng-stage0/
│
├── main.py # FastAPI app with /me endpoint
├── requirements.txt # Project dependencies
├── README.md # Project documentation


---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/hng-stage0.git
cd hng-stage0
pip install -r requirements.txt

▶️ Running Locally

Once dependencies are installed, start the FastAPI app with:

uvicorn main:app --reload


You should see output like:

INFO:     Uvicorn running on http://127.0.0.1:8000


Now open your browser or use curl:

http://127.0.0.1:8000/me

🔧 Environment Variables

You can override defaults with environment variables:

Variable	Description	Default
HNG_EMAIL	Your email address eg	stdave001@gmail.com
HNG_NAME	Your name eg	Ibukun Babatunde
HNG_STACK	Your preferred eg stack	Python/FastAPI

Example (macOS/Linux):

export HNG_EMAIL="your_email@example.com"
export HNG_NAME="Your Name"
export HNG_STACK="Python/FastAPI"
uvicorn main:app --reload


Example (Windows PowerShell):

setx HNG_EMAIL "your_email@example.com"
setx HNG_NAME "Your Name"
setx HNG_STACK "Python/FastAPI"

📦 Dependencies

All dependencies are listed in requirements.txt, but here’s the core stack:

Package	Purpose
fastapi	API framework
uvicorn	ASGI server
requests	To fetch cat facts
python-dotenv (optional)	For environment variable management
📚 Example Response

GET /me

{
  "status": "success",
  "user": {
    "email": "stdave001@gmail.com",
    "name": "Ibukun Babatunde",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-17T08:45:12.345Z",
  "fact": "Cats sleep 70% of their lives."
}

🧑‍💻 Author

Ibukun Babatunde
📧 stdave001@gmail.com

💻 Stack: Python / FastAPI



