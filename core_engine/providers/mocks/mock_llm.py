import asyncio

from core_engine.interfaces.llm_provider import ILLMProvider


class MockLLMProvider(ILLMProvider):

    async def generate_response(self, prompt: str) -> str:
        print("🧠 Pensando...")

        await asyncio.sleep(2)

        return f"Hola 👋, recibí tu mensaje: '{prompt}'"