from typing import Any

from core_engine.domain.tool_models import ToolResult
from core_engine.tools.tool_registry import ToolRegistry


class ToolManager:
    def __init__(self, registry: ToolRegistry) -> None:
        self._registry = registry

    async def execute(
        self,
        tool_name: str,
        arguments: dict[str, Any],
    ) -> ToolResult:
        if not self._registry.exists(tool_name):
            return ToolResult(
                success=False,
                message=f"La herramienta '{tool_name}' no está disponible.",
                error="tool_not_found",
            )

        tool = self._registry.get(tool_name)

        try:
            return await tool.execute(arguments)

        except Exception as exc:
            return ToolResult(
                success=False,
                message=f"No se pudo ejecutar la herramienta '{tool_name}'.",
                error=str(exc),
            )

    def list_definitions(self) -> list[dict[str, Any]]:
        return [
            {
                "name": tool.definition.name,
                "description": tool.definition.description,
                "parameters": tool.definition.parameters,
            }
            for tool in self._registry.all()
        ]