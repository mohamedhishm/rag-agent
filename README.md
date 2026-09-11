# 🤖 Smart File Assistant

A beginner-friendly AI agent that allows users to upload documents and ask questions about their content.

This project was built as a **small learning project** to understand the fundamentals of building AI agents, working with AI APIs, implementing a simple RAG pipeline, retrieving relevant information from documents, and using that information to generate answers.

> 🚀 **This is an early prototype and is designed to be extended with more advanced AI agent and RAG capabilities in the future.**

## 📌 Project Overview

**Smart File Assistant** is a simple AI-powered document assistant built with Python and Streamlit.

The user can upload a:

- 📄 PDF file
- 📝 TXT file
- 📃 DOCX file

Then ask questions about the uploaded document.

The application extracts the document text, splits it into smaller chunks, retrieves the chunks most relevant to the user's question, and sends the retrieved context to an AI model to generate the final answer.

The application can also answer general questions when a document is not provided or when the retrieved context is not considered relevant enough.

## 🎯 Why I Built This Project

I built this project as a **learning prototype** to understand the basics of AI application development.

Through this project, I practiced:

- How to build a simple AI agent
- How to work with AI APIs
- How to connect an application to an AI model
- How RAG (Retrieval-Augmented Generation) works
- How to extract text from different document formats
- How to split documents into smaller chunks
- How to retrieve relevant information from a document
- How to pass retrieved context to an AI model
- How to build a simple user interface using Streamlit

The goal was not to build a production-ready system, but to create a small working project that helps me understand the building blocks behind more advanced AI agents.

## 🧠 How It Works

The application follows a simple RAG-based pipeline:

```text
                ┌─────────────────┐
                │   Upload File   │
                │ PDF / TXT / DOCX│
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │  Extract Text   │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Split into      │
                │ Chunks          │
                └────────┬────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │ User asks a question │
              └──────────┬───────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Retrieve the    │
                │ most relevant   │
                │ chunks          │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Send Context +  │
                │ Question to AI  │
                └────────┬────────┘
                         │
                         ▼
                ┌─────────────────┐
                │ Generate Answer │
                └─────────────────┘
```

## 🔎 RAG Pipeline

The project implements a simple Retrieval-Augmented Generation approach.

### 1. Document Ingestion

When a user uploads a document, the application extracts its text.

The project currently supports:

- PDF using `pypdf`
- DOCX using `python-docx`
- TXT using Python's built-in text decoding

This logic is implemented in `rag_utils.py`.

### 2. Text Chunking

The extracted text is divided into smaller pieces called **chunks**.

The current configuration uses:

```python
chunk_size = 800
overlap = 150
```

The overlap helps preserve some context between neighboring chunks.

### 3. Retrieval

When the user asks a question, the application uses:

- `TfidfVectorizer`
- TF-IDF representations
- Cosine similarity

to find the document chunks that are most relevant to the question.

The top 3 chunks are retrieved by default.

### 4. Context Injection

If the best retrieved chunk passes the similarity threshold, the retrieved chunks are added to the prompt.

The AI model is instructed to answer using only the provided document context and to clearly say when the answer cannot be found in the document.

### 5. AI Generation

The retrieved context and user question are sent to the AI model through an OpenAI-compatible client configured to use the Groq API.

The current model used by the project is:

```text
openai/gpt-oss-20b
```

## 🛠️ Technologies Used

- **Python**
- **Streamlit**
- **Groq API**
- **OpenAI Python SDK**
- **RAG**
- **TF-IDF**
- **Cosine Similarity**
- **scikit-learn**
- **pypdf**
- **python-docx**
- **python-dotenv**

The required dependencies are listed in `requirements.txt`. fileciteturn0file2L1-L6

## 📁 Project Structure

```text
rag-agent/
│
├── app.py
├── rag_utils.py
├── test_connection.py
├── requirements.txt
├── .env
└── README.md
```

### `app.py`

Contains the Streamlit application and the main application flow.

It handles:

- File uploading
- User questions
- RAG retrieval
- Prompt construction
- AI model requests
- Displaying the final answer

The UI supports PDF, TXT, and DOCX uploads. fileciteturn0file0L10-L15

### `rag_utils.py`

Contains the main document-processing and retrieval functions:

- `extract_text()`
- `split_text()`
- `retrieve_chunks()`

The retrieval system uses TF-IDF and cosine similarity to rank the document chunks. fileciteturn0file1L42-L67

### `test_connection.py`

A small script used to verify that the AI API connection is working correctly. It uses the same Groq/OpenAI-compatible configuration and sends a simple test request. fileciteturn0file3L8-L18

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

### 2. Enter the project directory

```bash
cd YOUR_REPOSITORY
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` file

Create a file named:

```text
.env
```

Add your Groq API key:

```env
GROQ_API_KEY=your_api_key_here
```

> ⚠️ Never commit your `.env` file or expose your API key publicly.

### 6. Run the application

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

## 🧪 Testing the API Connection

You can test the API connection separately using:

```bash
python test_connection.py
```

If the connection is configured correctly, the script should return:

```text
Connection successful.
```

## 💡 Example Use Cases

You can upload documents such as:

- 📚 Study notes
- 📄 Technical documentation
- 📑 Research papers
- 📃 Text files
- 📖 Books or chapters
- 📝 Personal notes

Then ask questions such as:

```text
What is this document about?
```

```text
Summarize the main points.
```

```text
What does the document say about X?
```

```text
Explain this concept from the document.
```

If the information cannot be found in the retrieved document context, the application is instructed to tell the user that it could not find the answer in the uploaded document.

## 🚧 Current Limitations

This project is intentionally simple because it was created as a learning prototype.

Some current limitations include:

- The retrieval system uses TF-IDF instead of modern vector embeddings.
- There is no vector database.
- Documents are processed in memory.
- There is no persistent document storage.
- Retrieval quality can be improved significantly.
- The agent currently has a relatively simple decision flow.
- There is no conversation memory.
- There are no citations pointing to exact document pages or sections.
- The project has not been designed as a production-scale system.

These limitations are intentional learning opportunities for future versions.

## 🚀 Future Improvements

This project is **designed to evolve**.

Possible future improvements include:

### 🔹 Better RAG

- Replace TF-IDF with embedding models.
- Use semantic search.
- Add a vector database such as FAISS, Chroma, or another vector store.
- Improve chunking strategies.
- Add metadata to chunks.
- Add document/page citations.

### 🔹 Better AI Agent

The current project can be expanded into a more capable AI agent that can:

- Decide when to use document retrieval.
- Decide when to answer using general knowledge.
- Use multiple tools.
- Perform multi-step reasoning workflows.
- Handle multiple documents.
- Remember previous conversation context.

### 🔹 Better User Experience

- Chat-based interface
- Conversation history
- Multiple file uploads
- File management
- Streaming responses
- Better error handling
- Authentication
- Improved UI/UX

### 🔹 Production Improvements

- Persistent storage
- Scalable vector database
- Better security
- Logging and monitoring
- Evaluation of retrieval quality
- Automated testing
- Deployment

## 📚 What I Learned

This project helped me understand the basic architecture behind AI-powered applications:

```text
User
 ↓
Application
 ↓
Document Processing
 ↓
Retrieval
 ↓
Relevant Context
 ↓
AI Model
 ↓
Generated Answer
```

More importantly, it gave me a practical starting point for learning how **AI agents and RAG systems are built**, instead of only learning the concepts theoretically.

## 🎓 Project Status

**Status: Learning Prototype / First AI Agent Project**

This is a small project created while learning how to build AI agents and RAG applications.

It is **not intended to be the final version**.

The project can be continuously improved and expanded as I learn more about:

- AI agents
- LLMs
- RAG
- Embeddings
- Vector databases
- Tool calling
- Agent workflows
- AI application architecture

## 👨‍💻 Author

**Mohamed Hisham**

Built as a hands-on learning project while exploring AI agents and Retrieval-Augmented Generation.

---

⭐ If you find this project useful or interesting, feel free to explore the code and follow its future development.
