from fastapi import APIRouter
from app.models.chat_model import ChatRequest
from app.services.rag_service import ask_question

router = APIRouter()


@router.post("/chat")
async def chat(request: ChatRequest):
    answer = ask_question(request.message, sender_id=request.sender_id)

    return {
        "success": True,
        "answer": answer
    }