import asyncio
import os

try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv() -> None:
        return None

from core_engine.core.emma_core import EmmaCore
from core_engine.plugins.echo.echo_tool import EchoTool
from core_engine.plugins.system.open_application_tool import OpenApplicationTool
from core_engine.providers.gemini.gemini_llm import GeminiLLMProvider
from core_engine.providers.mocks.mock_stt import MockSTTProvider
from core_engine.providers.mocks.mock_tts import MockTTSProvider
from core_engine.tools.tool_manager import ToolManager
from core_engine.tools.tool_registry import ToolRegistry


async def main() -> None:
    load_dotenv()

    api_key = os.getenv("GEMINI_API_KEY")
    model = os.getenv("GEMINI_MODEL", "gemini-3.5-flash")

    if not api_key:
        raise RuntimeError(
            "No se encontró GEMINI_API_KEY en el archivo .env."
        )

    registry = ToolRegistry()
    registry.register(EchoTool())
    registry.register(OpenApplicationTool())

    tool_manager = ToolManager(registry)

    llm_provider = GeminiLLMProvider(
        api_key=api_key,
        model=model,
    )

    emma = EmmaCore(
        llm_provider=llm_provider,
        stt_provider=MockSTTProvider(),
        tts_provider=MockTTSProvider(),
        tool_manager=tool_manager,
    )

    try:
        await emma.process_interaction()
    finally:
        await llm_provider.close()


if __name__ == "__main__":
    asyncio.run(main())