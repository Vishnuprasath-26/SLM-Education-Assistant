
from pydantic import BaseModel, Field


class ChatRequest(BaseModel):

    question: str = Field(
        ...,
        min_length=3,
        max_length=1000,
        description="Educational question for the SLM"
    )


class ChatResponse(BaseModel):

    question: str
    answer: str
    model: str
    status: str
