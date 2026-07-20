import asyncio

from core_engine.plugins.echo.echo_tool import EchoTool
from core_engine.plugins.system.open_application_tool import OpenApplicationTool
from core_engine.tools.tool_manager import ToolManager
from core_engine.tools.tool_registry import ToolRegistry


async def main() -> None:
    registry = ToolRegistry()

    registry.register(EchoTool())
    registry.register(OpenApplicationTool())

    manager = ToolManager(registry)

    echo_result = await manager.execute(
        "echo",
        {
            "message": "Hola Emma",
        },
    )

    print(echo_result)

    application_result = await manager.execute(
        "open_application",
        {
            "application": "notepad",
        },
    )

    print(application_result)

    for definition in manager.list_definitions():
        print(
            f"- {definition.name}: "
            f"{definition.description}"
        )


if __name__ == "__main__":
    asyncio.run(main())