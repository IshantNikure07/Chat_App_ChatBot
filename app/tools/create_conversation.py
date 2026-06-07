import requests
from dotenv import load_dotenv
import os
from langchain_core.tools import tool

load_dotenv()

def create_conversation(type: str, receiver_id: str, sender_id: str) -> str:
    BACKEND_BASE_URL=os.getenv("BACKEND_BASE_URL")
    api_url = f"{BACKEND_BASE_URL}/api/conversation"
    api_key = os.getenv("INTERNAL_API_KEY")
    headers = {"x-internal-api-key": api_key}
    
    try: 
        res = requests.post(api_url, headers=headers, json={"type": type, "receiverId": receiver_id , "senderId": sender_id})
        data = res.json()
        print("create conversation response", data , "payload" , {"type": type, "receiverId": receiver_id , "senderId": sender_id})
        return str(data)
    except Exception as e:
        return f"Error creating conversation: {str(e)}"

