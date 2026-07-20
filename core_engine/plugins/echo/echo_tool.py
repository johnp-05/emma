from typing import Any

from core_engine.contracts.tools import ITool
from core_engine.domain.tool_models import ToolDefinition, ToolResult


class EchoTool(ITool):
    @property
    def definition(self) -> ToolDefinition:
        return ToolDefinition(
            name="echo",
            description="Devuelve exactamente el mensaje recibido.",
            parameters={
                "message": {
                    "type": "string",
                    "description": "Mensaje a devolver",
                }
            },
        )

    async def execute(self, arguments: dict[str, Any]) -> ToolResult:
        message = arguments.get("message", "")

        return ToolResult(
            success=True,
            message=message,
        )