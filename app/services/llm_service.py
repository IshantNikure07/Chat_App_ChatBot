import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

# Singleton or cached LLM instance to avoid recreation overhead
_llm_instance = None

def get_llm(model_name: str = "llama-3.1-8b-instant", temperature: float = 0.3) -> ChatGroq:
    """
    Returns an initialized ChatGroq LLM instance.
    Uses caching to avoid re-initializing the LLM multiple times.
    """
    global _llm_instance
    if _llm_instance is None:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY environment variable is not set.")
        
        _llm_instance = ChatGroq(
            model_name=model_name,
            temperature=temperature,
            groq_api_key=api_key
        )
    return _llm_instance
