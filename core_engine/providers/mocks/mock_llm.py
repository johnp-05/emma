import asyncio

from core_engine.domain.llm_result import LLMResult
from core_engine.interfaces.llm_provider import ILLMProvider


class MockLLMProvider(ILLMProvider):
    async def generate_response(
        self,
        user_message: str,
    ) -> LLMResult:
        print("🧠 Pensando...")

        await asyncio.sleep(1)

        normalized_message = user_message.strip().lower()

        if "abre" in normalized_message and (
            "bloc de notas" in normalized_message
            or "notepad" in normalized_message
        ):
            return LLMResult(
                message="Voy a abrir el Bloc de notas.",
                tool_name="open_application",
                tool_arguments={
                    "application": "notepad",
                },
            )

        return LLMResult(
            message=f"Hola 👋, recibí tu mensaje: '{user_message}'",
        )