
import requests

from src.api.config import (
    MODEL_NAME,
    OLLAMA_API_URL,
    TEMPERATURE,
    MAX_NEW_TOKENS,
    TIMEOUT,
    PROMPT_INSTRUCTIONS
)


class OllamaService:

    def __init__(self):
        self.model_name = MODEL_NAME
        self.api_url = OLLAMA_API_URL

    def generate_answer(self, question: str) -> str:

        instructions = "\n".join(
            f"{index}. {instruction}"
            for index, instruction in enumerate(
                PROMPT_INSTRUCTIONS, start=1
            )
        )

        prompt = f"""
{instructions}

Question: {question}

Answer:
"""

        payload = {
            "model": self.model_name,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": TEMPERATURE,
                "num_predict": MAX_NEW_TOKENS
            }
        }

        try:
            response = requests.post(
                self.api_url,
                json=payload,
                timeout=TIMEOUT
            )

            response.raise_for_status()

            result = response.json()

            answer = result.get("response", "").strip()

            if not answer:
                raise RuntimeError(
                    "Ollama returned an empty response."
                )

            return answer

        except requests.exceptions.Timeout as exc:
            raise RuntimeError(
                "Ollama request timed out."
            ) from exc

        except requests.exceptions.ConnectionError as exc:
            raise RuntimeError(
                "Cannot connect to Ollama. "
                "Please check whether Ollama is running."
            ) from exc

        except requests.exceptions.RequestException as exc:
            raise RuntimeError(
                f"Ollama API request failed: {exc}"
            ) from exc
