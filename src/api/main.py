
from fastapi import FastAPI, HTTPException

from src.api.schemas import ChatRequest, ChatResponse
from src.api.services import OllamaService
from src.api.logging_config import logger


app = FastAPI(
    title="SLM Education Assistant API",
    description="Educational question answering using Gemma 3 1B",
    version="1.0.0"
)

ollama_service = OllamaService()


@app.get("/")
def home():
    logger.info("Home endpoint accessed")

    return {
        "message": "SLM Education Assistant API is running",
        "model": ollama_service.model_name,
        "status": "success"
    }


@app.get("/health")
def health_check():
    logger.info("Health endpoint accessed")

    return {
        "status": "healthy",
        "model": ollama_service.model_name
    }


@app.post("/api/v1/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    logger.info("Chat request received")

    try:
        answer = ollama_service.generate_answer(
            request.question
        )

        logger.info("Chat response generated successfully")

        return ChatResponse(
            question=request.question,
            answer=answer,
            model=ollama_service.model_name,
            status="success"
        )

    except RuntimeError as exc:
        logger.error("Chat generation failed: %s", exc)

        raise HTTPException(
            status_code=503,
            detail=str(exc)
        ) from exc
