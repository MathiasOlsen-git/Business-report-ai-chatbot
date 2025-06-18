from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OllamaEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import Ollama

def build_qa_chain(documents):
    # Split long texts into smaller chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_docs = text_splitter.split_documents(documents)

    # Generate embeddings with Ollama
    embeddings = OllamaEmbeddings(model="nomic-embed-text")  # make sure you've pulled this model
    vectorstore = FAISS.from_documents(split_docs, embeddings)

    # Load a local language model via Ollama
    llm = Ollama(model="llama3")  # or "mistral", "gemma", etc.

    # Create RAG chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        return_source_documents=True
    )

    return qa_chain
