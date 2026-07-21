from typing import Any

from google import genai

from core_engine.domain.llm_result import LLMResult
from core_engine.interfaces.llm_provider import ILLMProvider


OPEN_APPLICATION_TOOL: dict[str, Any] = {
    "type": "function",
    "name": "open_application",
    "description": (
        "Abre una aplicación permitida en el computador del usuario. "
        "Úsala cuando el usuario solicite abrir o iniciar una aplicación."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "application": {
                "type": "string",
                "description": (
                    "Identificador de la aplicación. "
                    "Valores permitidos: notepad, calculator, explorer o code."
                ),
                "enum": [
                    "notepad",
                    "calculator",
                    "explorer",
                    "code",
                ],
            },
        },
        "required": ["application"],
        "additionalProperties": False,
    },
}


class GeminiLLMProvider(ILLMProvider):
    def __init__(
        self,
        api_key: str,
        model: str = "gemini-3.5-flash",
    ) -> None:
        if not api_key.strip():
            raise ValueError("La API key de Gemini no puede estar vacía.")

        self._model = model
        self._client = genai.Client(api_key=api_key)

    async def generate_response(
        self,
        user_message: str,
    ) -> LLMResult:
        print("🧠 Gemini está pensando...")

        interaction = await self._client.aio.interactions.create(
            model=self._model,
            input=user_message,
            tools=[OPEN_APPLICATION_TOOL],
        )

        function_call = self._find_function_call(interaction.steps)

        if function_call is not None:
            return LLMResult(
                message=self._build_tool_message(
                    tool_name=function_call.name,
                    arguments=function_call.arguments,
                ),
                tool_name=function_call.name,
                tool_arguments=dict(function_call.arguments),
            )

        response_text = interaction.output_text

        if not response_text:
            return LLMResult(
                message="No pude generar una respuesta.",
            )

        return LLMResult(
            message=response_text.strip(),
        )

    @staticmethod
    def _find_function_call(
        steps: list[Any],
    ) -> Any | None:
        for step in steps:
            if step.type == "function_call":
                return step

        return None

    @staticmethod
    def _build_tool_message(
        tool_name: str,
        arguments: dict[str, Any],
    ) -> str:
        if tool_name == "open_application":
            application = arguments.get(
                "application",
                "la aplicación",
            )

            return f"Voy a abrir {application}."

        return "Voy a ejecutar la acción solicitada."

    async def close(self) -> None:
        await self._client.aio.aclose()