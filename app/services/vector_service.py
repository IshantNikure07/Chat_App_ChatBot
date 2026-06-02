import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

# Cached embeddings and vector store instances to minimize reload times
_embeddings_instance = None
_vector_store_instance = None

def get_embeddings(model_name: str = "all-MiniLM-L6-v2") -> HuggingFaceEmbeddings:
    """
    Returns the HuggingFaceEmbeddings instance.
    Uses caching to avoid reloading the model weights.
    """
    global _embeddings_instance
    if _embeddings_instance is None:
        _embeddings_instance = HuggingFaceEmbeddings(model_name=model_name)
    return _embeddings_instance

def get_vector_store(persist_directory: str = "chroma_db") -> Chroma:
    """
    Loads and returns the persisted Chroma vector store.
    """
    global _vector_store_instance
    if _vector_store_instance is None:
        embeddings = get_embeddings()
        if not os.path.exists(persist_directory):
            print(f"Warning: Vector database directory '{persist_directory}' does not exist.")
        
        _vector_store_instance = Chroma(
            persist_directory=persist_directory,
            embedding_function=embeddings
        )
    return _vector_store_instance

def get_retriever(persist_directory: str = "chroma_db", k: int = 2):
    """
    Returns a retriever instance from the Chroma vector store.
    """
    vector_store = get_vector_store(persist_directory)
    if vector_store:
        return vector_store.as_retriever(search_kwargs={"k": k})
    return None
