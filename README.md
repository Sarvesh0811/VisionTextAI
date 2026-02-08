
# 🚀 VisionText AI  
### Multi-Language AI OCR & Translation System  

VisionText AI is a full-stack, multi-language AI-powered OCR and translation system that extracts text from images, enhances accuracy using an optimization pipeline, and translates content into English. The system uses a FastAPI backend and a Streamlit frontend with a clean, modular, and scalable architecture.

---

## 📌 Problem Statement

Traditional OCR engines often struggle with:

- Multi-language text  
- Noisy images  
- Low-quality scans  
- Poor formatting  
- Incorrect spellings  

VisionText AI solves this by combining AI-based vision OCR with intelligent post-processing and translation, providing clean and accurate results for real-world documents.

---

## 🎯 Key Features

- 📷 Image-to-Text Extraction (AI Vision OCR)  
- 🌍 Multi-Language Support  
- 🧹 OCR Error Correction  
- 📄 Structure Cleanup  
- 🌐 English Translation  
- ⚡ FastAPI REST API  
- 🎨 Streamlit Web UI  
- 🧩 Modular & Scalable Architecture  
- 📝 File-based Logging  

---

## 🧠 System Architecture

```

Streamlit Frontend
       |
FastAPI Backend
       |
OCR Service 
       |
Optimization Service 
       |
Translation Service
       |
Final Output

```

---

## 🛠 Tech Stack

### Backend
- Python  
- FastAPI  
- OpenAI API  
- Uvicorn  
- python-dotenv  

### Frontend
- Streamlit  
- Requests  

### Other Tools
- Pillow  
- Logging  
- Git  

---

## 📂 Project Folder Structure

```

VisionText-AI/
├── server/
│   ├── app/
│   │   ├── main.py
│   │   └── exception_handlers.py
│   ├── core/
│   │   └── config.py
│   ├── router/
│   │   └── v1/
│   │       └── ocr.py
│   ├── schemas/
│   │   └── ocr.py
│   ├── services/
│   │   ├── ocr.py
│   │   ├── optimization.py
│   │   ├── translation.py
│   │   └── pipeline.py
│   ├── logs/
│   │   └── app.log
│   ├── .env
│   ├── requirements.txt
│   └── .gitignore
│
├── client/
│   ├── app.py
│   ├── services/
│   │   └── api.py
│   ├── components/
│   │   └── ui.py
│   ├── .env
│   └── requirements.txt
│
└── README.md

```

---

## ⚙️ Environment Variables

### Backend (`server/.env`)

```

OPENAI_API_KEY=your_openai_api_key_here

```

### Frontend (`client/.env`)

```

BACKEND_URL=[http://localhost:8000/api/v1/ocr](http://localhost:8000/api/v1/ocr)

````

---

## 📦 Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/VisionText-AI.git
cd VisionText-AI
````

---

### 2️⃣ Backend Setup

```bash
cd server
pip install -r requirements.txt
```

Create `.env` file and add your OpenAI API key.

---

### 3️⃣ Start Backend Server

```bash
uvicorn app.main:app --reload
```

Backend will run at:

```
http://127.0.0.1:8000
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

### 4️⃣ Frontend Setup

Open a new terminal:

```bash
cd client
pip install -r requirements.txt
```

---

### 5️⃣ Start Streamlit Client

```bash
streamlit run app.py
```

Frontend will open at:

```
http://localhost:8501
```

---

## ▶️ How to Use

1. Open Streamlit UI
2. Upload an image
3. Wait for processing
4. View:

   * Raw OCR Text
   * English Translation

---

## 🚀 Future Enhancements

* Language selection
* Download results as PDF/TXT
* OCR history dashboard
* Docker deployment

---

## 👨‍💻 Author

Sarvesh Patil

---


