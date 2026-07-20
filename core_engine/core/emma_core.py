from core_engine.interfaces.llm_provider import ILLMProvider
from core_engine.interfaces.stt_provider import ISTTProvider
from core_engine.interfaces.tts_provider import ITTSProvider


class EmmaCore:
    """
    Núcleo principal de Emma.

    Orquesta el flujo entre los distintos proveedores sin conocer
    ninguna implementación concreta.
    """

    def __init__(
        self,
        llm_provider: ILLMProvider,
        stt_provider: ISTTProvider,
        tts_provider: ITTSProvider,
    ) -> None:
        self._llm = llm_provider
        self._stt = stt_provider
        self._tts = tts_provider

    async def process_interaction(self) -> None:
        """
        Flujo principal de una interacción.
        """

        print("🎤 Escuchando...")

        user_message = await self._stt.listen()

        print(f"👤 Usuario: {user_message}")

        response = await self._llm.generate_response(user_message)

        print(f"🤖 Emma: {response}")

        await self._tts.speak(response)