# 🔍 Retrieval-Augmented Generation (RAG) with Gemini & PDF

This project implements a lightweight RAG (Retrieval-Augmented Generation) pipeline that allows you to ask questions about the contents of any PDF using Google’s Gemini LLM. It uses LangChain for loading and chunking documents, SentenceTransformers for embedding generation, and ChromaDB for vector storage and retrieval. The goal is to enable efficient semantic search and natural language Q&A over unstructured text documents.

---

## 📌 Features

- 📄 Load and parse PDF documents
- ✂️ Chunk large text into overlapping segments
- 🧠 Generate vector embeddings using `all-MiniLM-L6-v2`
- 💾 Store and retrieve from a persistent vector DB (Chroma)
- 🔍 Perform similarity search to fetch relevant context
- 💬 Use Google Gemini to answer questions based on context

---

## ⚙️ Tech Stack

- **LangChain** – document loader, text splitter
- **ChromaDB** – vector storage and retrieval
- **SentenceTransformers** – for embedding generation
- **Google Generative AI SDK** – Gemini LLM
- **Python & dotenv** – API key and environment setup

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/rag-gemini-pdf.git
cd rag-gemini-pdf
