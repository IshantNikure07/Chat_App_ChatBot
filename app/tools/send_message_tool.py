import requests
from dotenv import load_dotenv
import os

load_dotenv()

def send_message(message: str, sender_id: str, receiver_id: str, conversation_id: str = None):
    BACKEND_BASE_URL = os.getenv("BACKEND_BASE_URL")
    api_key = os.getenv("INTERNAL_API_KEY")
    headers = {"x-internal-api-key": api_key}
    api_url = f"{BACKEND_BASE_URL}/api/messages/send"

    payload = {
        "message": message,
        "sender_id": sender_id,
        "receiver_id": receiver_id
    }
    if conversation_id:
        payload["conversation_id"] = conversation_id

    try:
        res = requests.post(api_url, json=payload, headers=headers)
        data = res.json()
        print("send message response", data , "payload" , payload)
        return str(data)
    except Exception as e:
        return f"Error sending message: {str(e)}"

if __name__ == "__main__":
    print(send_message("hello", "692ea4f0a6d33a9766df1521", "692ea496a6d33a9766df1518"))