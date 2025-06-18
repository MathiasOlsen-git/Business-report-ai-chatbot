from langchain.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
from langchain.schema import Document
from pathlib import Path
import pandas as pd

def load_documents_from_folder(folder_path):
    """Load documents of various file types from a folder."""
    documents = []
    folder = Path(folder_path)

    for file_path in folder.glob("*"):
        suffix = file_path.suffix.lower()

        # PDF files
        if suffix == ".pdf":
            loader = PyPDFLoader(str(file_path))
            documents.extend(loader.load())

        # Word documents (.docx)
        elif suffix == ".docx":
            loader = Docx2txtLoader(str(file_path))
            documents.extend(loader.load())

        # Plain text files
        elif suffix == ".txt":
            loader = TextLoader(str(file_path))
            documents.extend(loader.load())

        # CSV files (converted to string)
        elif suffix == ".csv":
            df = pd.read_csv(file_path)
            text = df.to_string(index=False)
            documents.append(Document(page_content=text, metadata={"source": str(file_path)}))

        else:
            print(f"Unsupported file type: {file_path.name}")

    return documents

