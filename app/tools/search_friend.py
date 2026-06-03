import requests 
from dotenv import load_dotenv
import os


load_dotenv()

def search_friends(name: str) -> str:
    BACKEND_BASE_URL=os.getenv("BACKEND_BASE_URL")
    api_url = f"{BACKEND_BASE_URL}/api/users/search/{name}"
    api_key = os.getenv("INTERNAL_API_KEY")
    headers = {"x-internal-api-key": api_key}
    
    try: 
        res = requests.get(api_url, headers=headers)
        data = res.json()
        return str(data)
    except Exception as e:
        return f"Error searching friends: {str(e)}"

if __name__ == "__main__":
    print(search_friends("test"))