from fastapi import APIRouter, UploadFile, Form
from services import rag_service

router = APIRouter()

@router.post("/rag-chat")
async def rag_chat(message: str = Form(...), file: UploadFile = None):
    """
    Recibe un mensaje y un archivo txt, y devuelve una respuesta generada
    usando la API de OpenAI.
    """
    content = await file.read()
    text = content.decode("utf-8")
    print("rag chat init")
    response = rag_service.get_rag_response(message, text)
    return {"response": response}
