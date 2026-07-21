import asyncio

from core_engine.interfaces.stt_provider import ISTTProvider


class MockSTTProvider(ISTTProvider):

    async def listen(self) -> str:
        print("🎤 Simulando reconocimiento de voz...")

        await asyncio.sleep(1)

        return "Emma, abre el Bloc de notas."