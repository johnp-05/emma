import asyncio

from core_engine.interfaces.tts_provider import ITTSProvider


class MockTTSProvider(ITTSProvider):

    async def speak(self, text: str) -> None:
        print("🔊 Reproduciendo voz...")

        await asyncio.sleep(1)

        print(text)