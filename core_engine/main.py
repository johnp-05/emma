import asyncio

from core_engine.core.emma_core import EmmaCore
from core_engine.plugins.echo.echo_tool import EchoTool
from core_engine.plugins.system.open_application_tool import OpenApplicationTool
from core_engine.tools.tool_manager import ToolManager
from core_engine.tools.tool_registry import ToolRegistry

# Mantén aquí tus imports actuales de mocks.
from core_engine.providers.mocks.mock_llm import MockLLMProvider
from core_engine.providers.mocks.mock_stt import MockSTTProvider
from core_engine.providers.mocks.mock_tts import MockTTSProvider



async def main() -> None:
    registry = ToolRegistry()

    registry.register(EchoTool())
    registry.register(OpenApplicationTool())

    tool_manager = ToolManager(registry)

    emma = EmmaCore(
        llm_provider=MockLLMProvider(),
        stt_provider=MockSTTProvider(),
        tts_provider=MockTTSProvider(),
        tool_manager=tool_manager,
    )

    await emma.process_interaction()

    await emma.execute_tool(
        "open_application",
        {
            "application": "notepad",
        },
    )


if __name__ == "__main__":
    asyncio.run(main())
