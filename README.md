# 🧬 ImmuneBot — Your Autoimmune Disease Assistant

ImmuneBot is an intelligent chatbot that helps users better understand the immune system and autoimmune diseases. It combines RAG (Retrieval-Augmented Generation) techniques with powerful LLMs and vector search to answer questions based on trusted medical documents.

## 🔍 Features

* **Semantic Search with ChromaDB & Nomic Embeddings**
* **Azure OpenAI Chat Completion API**
* **PDF Knowledge Ingestion (via PyMuPDF)**
* **Interactive Chat Interface using Streamlit**
* **Deployable on Hugging Face Spaces**

---

## 🏗️ Tech Stack

| Component        | Tool / Service                     |
| ---------------- | ---------------------------------- |
| UI               | Streamlit                          |
| Backend LLM      | Azure OpenAI                       |
| Embedding Model  | `nomic-embed-text` (via Nomic API) |
| Vector Store     | ChromaDB                           |
| Document Parsing | PyMuPDF (`fitz`)                   |
| Deployment       | Hugging Face Spaces                |

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/ImmuneBot.git
cd ImmuneBot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Environment Setup

Create a `.env` file with the following variables:

```env
AZURE_OPENAI_API_KEY=your_azure_api_key
AZURE_OPENAI_ENDPOINT=your_endpoint_url
NOMIC_API_KEY=your_nomic_api_key
```

---

## 🧠 How It Works

1. User asks a question through the chat UI.
2. The app semantically searches a collection of medical PDFs stored in ChromaDB.
3. Top relevant passages are retrieved and passed to the LLM via Azure's OpenAI API.
4. The model responds with structured, reliable medical information.

---

## 📁 Project Structure

```
ImmuneBot/
├── app.py                     # Streamlit frontend
├── RAG_Immune_system.py       # RAG pipeline (retrieval + LLM answer)
├── prompt.py                  # Custom system prompts
├── utils.py                   # Helper functions (PDF parsing, embedding, etc.)
├── requirements.txt
├── .env                       # Your API keys (not to be committed!)
└── README.md
```

---

## 📦 Deployment on Hugging Face Spaces

To deploy:

1. Create a new **Streamlit Space** at [Hugging Face Spaces](https://huggingface.co/spaces)
2. Upload all files (`app.py`, `RAG_Immune_system.py`, `prompt.py`, etc.)
3. Add your `.env` secrets using the "Secrets" tab
4. Set `app.py` as the main file
5. Done! 🚀 Your chatbot is live.

---

## 💡 Future Ideas

* Multilingual support (Arabic/English)
* Web search fallback for unknown queries
* Real-time symptom checker
* Upload your own medical reports

---

## 📜 License

This project is licensed under the MIT License.

---

