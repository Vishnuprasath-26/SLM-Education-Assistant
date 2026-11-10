
from fastapi.testclient import TestClient

from src.api.main import app
from src.api.services import OllamaService


client = TestClient(app)


def test_home_endpoint():

    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "success"
    assert data["model"] == "gemma3:1b"


def test_health_endpoint():

    response = client.get("/health")

    assert response.status_code == 200

    data = response.json()

    assert data["status"] == "healthy"


def test_chat_success(monkeypatch):

    def mock_generate_answer(self, question):
        return "Python is a programming language."

    monkeypatch.setattr(
        OllamaService,
        "generate_answer",
        mock_generate_answer
    )

    response = client.post(
        "/api/v1/chat",
        json={"question": "What is Python?"}
    )

    assert response.status_code == 200

    data = response.json()

    assert data["question"] == "What is Python?"
    assert data["answer"] == "Python is a programming language."
    assert data["model"] == "gemma3:1b"
    assert data["status"] == "success"


def test_chat_invalid_question():

    response = client.post(
        "/api/v1/chat",
        json={"question": "AI"}
    )

    assert response.status_code == 422


def test_chat_missing_question():

    response = client.post(
        "/api/v1/chat",
        json={}
    )

    assert response.status_code == 422

def test_chat_service_error(monkeypatch):

    def mock_generate_answer(self, question):
        raise RuntimeError("Ollama service unavailable")

    monkeypatch.setattr(
        OllamaService,
        "generate_answer",
        mock_generate_answer
    )

    response = client.post(
        "/api/v1/chat",
        json={"question": "What is Python?"}
    )

    assert response.status_code == 503

    data = response.json()

    assert data["detail"] == "Ollama service unavailable"
