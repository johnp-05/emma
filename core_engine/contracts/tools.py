from abc import ABC, abstractmethod
from typing import Any

from core_engine.domain.tool_models import ToolDefinition, ToolResult


class ITool(ABC):
    @property
    @abstractmethod
    def definition(self) -> ToolDefinition:
        """Devuelve la descripción pública de la herramienta."""
        raise NotImplementedError

    @abstractmethod
    async def execute(self, arguments: dict[str, Any]) -> ToolResult:
        """Ejecuta la herramienta sin bloquear el event loop."""
        raise NotImplementedError