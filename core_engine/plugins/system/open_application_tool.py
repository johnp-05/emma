import asyncio
from typing import Any

from core_engine.contracts.tools import ITool
from core_engine.domain.tool_models import ToolDefinition, ToolResult


class OpenApplicationTool(ITool):
    @property
    def definition(self) -> ToolDefinition:
        return ToolDefinition(
            name="open_application",
            description="Abre una aplicación permitida en Windows.",
            parameters={
                "application": {
                    "type": "string",
                    "description": "Nombre de la aplicación que se desea abrir",
                }
            },
        )

    async def execute(self, arguments: dict[str, Any]) -> ToolResult:
        application = str(arguments.get("application", "")).strip().lower()

        allowed_applications = {
            "notepad": "notepad.exe",
            "calculator": "calc.exe",
            "explorer": "explorer.exe",
            "code": "code",
        }

        command = allowed_applications.get(application)

        if command is None:
            return ToolResult(
                success=False,
                message=f"La aplicación '{application}' no está permitida.",
                error="application_not_allowed",
            )

        await asyncio.create_subprocess_exec(command)

        return ToolResult(
            success=True,
            message=f"Aplicación '{application}' abierta correctamente.",
        )