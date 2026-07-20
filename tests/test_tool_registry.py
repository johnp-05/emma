import asyncio

from core_engine.plugins.system.open_application_tool import OpenApplicationTool
from core_engine.tools.tool_manager import ToolManager
from core_engine.tools.tool_registry import ToolRegistry


async def main() -> None:
    registry = ToolRegistry()
    registry.register(OpenApplicationTool())

    manager = ToolManager(registry)

    result = await manager.execute(
        "open_application",
        {
            "application": "notepad",
        },
    )

    print(result)


if __name__ == "__main__":
    asyncio.run(main())