from fastapi import APIRouter, HTTPException, Depends, BackgroundTasks
from core.models import ChatCompletionRequest, ChatCompletionResponse, Provider
from services.factory import service_factory  # à créer
from api.dependencies import get_cache  # à créer

router = APIRouter()

@router.post("/completions", response_model=ChatCompletionResponse)
async def create_chat_completion(
    background_tasks: BackgroundTasks,
    request: ChatCompletionRequest,
    cache = Depends(get_cache)
):
    provider = request.provider or Provider.openai
    service = service_factory.get_service(provider)
    if not service:
        raise HTTPException(status_code=400, detail="Provider not supported")

    response = await service.get_chat_completion(request)
    return response


