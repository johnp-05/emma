from abc import ABC, abstractmethod
from typing import Any

from core_engine.domain.tool_models import ToolDefinition, ToolResult


class ITool(ABC):
    @property
    @abstractmethod
    def definition(self) -> ToolDefinition:
        raise NotImplementedError

    @abstractmethod
    async def execute(self, arguments: dict[str, Any]) -> ToolResult:
        raise NotImplementedError