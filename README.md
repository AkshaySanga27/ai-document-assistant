# AI Document Assistant

A Retrieval-Augmented Generation (RAG) based document question-answering application that allows users to ask questions about PDF documents and receive answers grounded in the document content.

The project combines PDF text extraction, text chunking, embeddings, vector similarity search, PostgreSQL with pgvector, and a Large Language Model (LLM) to create a document-aware AI assistant.

---

## Project Overview

The AI Document Assistant follows a RAG pipeline:

PDF Document
      ↓
Text Extraction
      ↓
Text Chunking
      ↓
Embeddings
      ↓
PostgreSQL + pgvector
      ↓
Vector Similarity Search
      ↓
Relevant Context
      ↓
RAG Prompt
      ↓
LLM (Llama 3.2)
      ↓
Answer + Sources

Instead of sending the entire document directly to the LLM, the application first retrieves the most relevant sections of the document and provides them as context to the LLM.

This helps the model generate answers based on the information contained in the uploaded document.

---

## Features

- PDF text extraction
- Text chunking with overlap
- Semantic embeddings
- Vector storage using PostgreSQL and pgvector
- Vector similarity search
- Retrieval-Augmented Generation (RAG)
- Local LLM integration using Ollama
- Llama 3.2 support
- Source document and page information
- FastAPI backend
- Modular service architecture
- Environment-based database configuration
- Basic testing for individual services

---

## Technologies Used

### Backend

- Python
- FastAPI
- Uvicorn
- Pydantic

### AI / LLM

- Ollama
- Llama 3.2
- Sentence Transformers
- `all-MiniLM-L6-v2`
- Retrieval-Augmented Generation (RAG)
- Embeddings
- Vector similarity search

### Database

- PostgreSQL
- pgvector
- SQLAlchemy
- psycopg2

### PDF Processing

- PyMuPDF

### Testing

- pytest

### Development Tools

- Git
- GitHub
- VS Code

---

## Project Structure

```text
ai-document-assistant/
│
├── app/
│   ├── __init__.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   └── documents.py
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── database.py
│   │
│   ├── models/
│   │   └── __init__.py
│   │
│   ├── prompts/
│   │   ├── __init__.py
│   │   ├── classification.py
│   │   ├── extraction.py
│   │   ├── rag.py
│   │   └── summarization.py
│   │
│   ├── schemas/
│   │   └── __init__.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── chunking_service.py
│   │   ├── embedding_service.py
│   │   ├── ingestion_service.py
│   │   ├── llm_service.py
│   │   ├── pdf_service.py
│   │   ├── rag_service.py
│   │   ├── retrieval_service.py
│   │   ├── vector_search_service.py
│   │   └── vector_service.py
│   │
│   ├── utils/
│   │   └── __init__.py
│   │
│   ├── main.py
│   ├── test_chunking.py
│   ├── test_database.py
│   ├── test_embeddings.py
│   ├── test_extraction.py
│   ├── test_ingestion.py
│   ├── test_rag.py
│   ├── test_rag_database.py
│   ├── test_retrieval.py
│   ├── test_vector_database.py
│   └── test_vector_search.py
│
├── documents/
├── data/
├── tests/
│   └── __init__.py
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt
