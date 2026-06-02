import os
import json
import shutil
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_community.vectorstores import Chroma
from app.services.vector_service import get_embeddings

# Load environment variables
load_dotenv()

FAQ_FILE = os.path.join("app", "data", "faq.json")
DB_DIR = "chroma_db"

def main():
    if not os.path.exists(FAQ_FILE):
        print(f"Error: FAQ file not found at {FAQ_FILE}")
        return

    print("Loading FAQ data...")
    with open(FAQ_FILE, "r", encoding="utf-8") as f:
        faq_data = json.load(f)

    print(f"Loaded {len(faq_data)} FAQ entries.")

    # Create Documents
    documents = []
    for item in faq_data:
        # We format content as "Question: ... \nAnswer: ..." to make it easy for similarity search
        content = f"Question: {item['question']}\nAnswer: {item['answer']}"
        doc = Document(
            page_content=content,
            metadata={"question": item["question"], "answer": item["answer"]}
        )
        documents.append(doc)

    # Initialize Embeddings model from service
    print("Initializing HuggingFace Embeddings model from vector_service...")
    embeddings = get_embeddings()

    # Clear existing vector database if exists
    if os.path.exists(DB_DIR):
        print(f"Clearing existing database directory: {DB_DIR}")
        try:
            shutil.rmtree(DB_DIR)
        except Exception as e:
            print(f"Warning: Could not remove directory {DB_DIR}: {e}")

    # Create and persist Chroma Vector DB
    print(f"Creating Chroma vector database at {DB_DIR}...")
    vector_store = Chroma.from_documents(
        documents=documents,
        embedding=embeddings,
        persist_directory=DB_DIR
    )
    print("Database created and persisted successfully!")

if __name__ == "__main__":
    main()
