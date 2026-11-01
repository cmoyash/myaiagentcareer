from config import Config
from google import genai
from typing import Any


class GeminiService:
    def __init__(self) -> None:
        Config.validate()
        self.client = genai.Client(api_key=Config.GEMINI_API_KEY)

    def generate_response(self, prompt: str , config: Any = None) -> Any:
        try:
            response = self.client.models.generate_content(
                model= Config.MODEL_NAME ,
                contents= prompt ,
                config=config
            )
            return response
        except Exception as e:
            raise RuntimeError(
                f"Server Error: {e}"
            )
        