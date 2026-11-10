
import src.api.services as services
from src.api.services import OllamaService


def test_generate_answer_success(monkeypatch):

    class MockResponse:

        def raise_for_status(self):
            pass

        def json(self):
            return {
                "response": "Python is a programming language."
            }

    def mock_post(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(
        services.requests,
        "post",
        mock_post
    )

    ollama_service = OllamaService()

    answer = ollama_service.generate_answer("What is Python?")

    assert answer == "Python is a programming language."


def test_generate_answer_timeout(monkeypatch):

    def mock_post(*args, **kwargs):
        raise services.requests.exceptions.Timeout()

    monkeypatch.setattr(
        services.requests,
        "post",
        mock_post
    )

    ollama_service = OllamaService()

    try:
        ollama_service.generate_answer("What is Python?")
        assert False, "Expected RuntimeError was not raised"

    except RuntimeError as exc:
        assert str(exc) == "Ollama request timed out."


def test_generate_answer_connection_error(monkeypatch):

    def mock_post(*args, **kwargs):
        raise services.requests.exceptions.ConnectionError()

    monkeypatch.setattr(
        services.requests,
        "post",
        mock_post
    )

    ollama_service = OllamaService()

    try:
        ollama_service.generate_answer("What is Python?")
        assert False, "Expected RuntimeError was not raised"

    except RuntimeError as exc:
        assert str(exc) == (
            "Cannot connect to Ollama. "
            "Please check whether Ollama is running."
        )


def test_generate_answer_http_error(monkeypatch):

    class MockResponse:

        def raise_for_status(self):
            raise services.requests.exceptions.HTTPError(
                "500 Server Error"
            )

    def mock_post(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(
        services.requests,
        "post",
        mock_post
    )

    ollama_service = OllamaService()

    try:
        ollama_service.generate_answer("What is Python?")
        assert False, "Expected RuntimeError was not raised"

    except RuntimeError as exc:
        assert str(exc) == (
            "Ollama API request failed: 500 Server Error"
        )

def test_generate_answer_empty_response(monkeypatch):

    class MockResponse:

        def raise_for_status(self):
            pass

        def json(self):
            return {
                "response": ""
            }

    def mock_post(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(
        services.requests,
        "post",
        mock_post
    )

    ollama_service = OllamaService()

    try:
        ollama_service.generate_answer("What is Python?")
        assert False, "Expected RuntimeError was not raised"

    except RuntimeError as exc:
        assert str(exc) == "Ollama returned an empty response."