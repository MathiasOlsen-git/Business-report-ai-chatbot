import streamlit as st
from loaders import load_documents_from_folder
from rag_chain import build_qa_chain

# Page setup
st.set_page_config(page_title="Company Internal AI-Chatbot", layout="centered")

# Clean title
st.title("🤖 Company Internal AI-Chatbot")
st.markdown("Ask your question below.")

# Input field
query = st.text_input("What would you like to know?", placeholder="e.g. What is the net income in 2023?")

# When the user submits a question
if query:
    with st.spinner("Loading documents..."):
        docs = load_documents_from_folder("docs")
        qa_chain = build_qa_chain(docs)

    with st.spinner("Thinking..."):
        result = qa_chain(query)

    # Show answer clearly
    st.subheader("Answer")
    st.write(result["result"])

    # Show sources
    st.subheader("Sources")
    for doc in result["source_documents"]:
        st.markdown(f"- `{doc.metadata.get('source', 'Unknown')}`")

