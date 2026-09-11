import os

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI
from rag_utils import extract_text, retrieve_chunks, split_text

load_dotenv()

st.title("Smart File Assistant")
st.write("Upload a file and ask questions about it, or ask general questions.")

uploaded_file = st.file_uploader(
    "Upload a file",
    type=["pdf", "txt", "docx"]
)

document_chunks = None

if uploaded_file:
    try:
        document_text = extract_text(uploaded_file)
        document_chunks = split_text(document_text)

        st.success(f"Selected file: {uploaded_file.name}")
        st.caption(f"Extracted {len(document_text):,} characters.")
        st.caption(f"Created {len(document_chunks)} chunks.")
    except Exception as error:
        st.error(f"Could not read this file: {error}")

question = st.text_input("Ask a question")
ask_button = st.button("Ask")

if ask_button:
    if not question:
        st.warning("Please type a question first.")
    else:
        client = OpenAI(
            api_key=os.getenv("GROQ_API_KEY"),
            base_url="https://api.groq.com/openai/v1"
        )

        if uploaded_file and document_chunks:
            retrieved_chunks = retrieve_chunks(
                question,
                document_chunks
            )

            best_score = retrieved_chunks[0]["score"]

            if best_score >= 0.10:
                context = "\n\n---\n\n".join(
                    item["text"] for item in retrieved_chunks
                )

                prompt = f"""
You are a helpful assistant.
Answer in the same language as the user's question.
Use only the document context below to answer the question.
If the answer is not in the context, clearly say that you could not find it in the uploaded document.

Document context:
{context}

Question:
{question}
"""
            else:
                prompt = question
        else:
            prompt = question

        with st.spinner("Thinking..."):
            response = client.responses.create(
                model="openai/gpt-oss-20b",
                input=prompt
            )

        st.subheader("Answer")
        st.write(response.output_text)