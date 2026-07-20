from typing import Any

from core_engine.contracts.tool_manager import IToolManager
from core_engine.domain.tool_models import ToolResult
from core_engine.interfaces.llm_provider import ILLMProvider
from core_engine.interfaces.stt_provider import ISTTProvider
from core_engine.interfaces.tts_provider import ITTSProvider


class EmmaCore:
    """
    Núcleo principal de Emma.

    Orquesta los proveedores y herramientas sin depender
    de implementaciones concretas.
    """

    def __init__(
        self,
        llm_provider: ILLMProvider,
        stt_provider: ISTTProvider,
        tts_provider: ITTSProvider,
        tool_manager: IToolManager,
    ) -> None:
        self._llm = llm_provider
        self._stt = stt_provider
        self._tts = tts_provider
        self._tool_manager = tool_manager

    async def process_interaction(self) -> None:
        """
        Ejecuta una interacción conversacional normal.
        """

        print("🎤 Escuchando...")

        user_message = await self._stt.listen()

        print(f"👤 Usuario: {user_message}")

        response = await self._llm.generate_response(user_message)

        print(f"🤖 Emma: {response}")

        await self._tts.speak(response)

    async def execute_tool(
        self,
        tool_name: str,
        arguments: dict[str, Any],
    ) -> ToolResult:
        """
        Ejecuta una herramienta mediante ToolManager.
        """

        print(f"🛠️ Ejecutando herramienta: {tool_name}")

        result = await self._tool_manager.execute(
            tool_name=tool_name,
            arguments=arguments,
        )

        print(f"🤖 Emma: {result.message}")

        await self._tts.speak(result.message)

        return result