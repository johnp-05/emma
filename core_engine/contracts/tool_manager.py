from abc import ABC, abstractmethod
from typing import Any

from core_engine.domain.tool_models import ToolDefinition, ToolResult


class IToolManager(ABC):
    @abstractmethod
    async def execute(
        self,
        tool_name: str,
        arguments: dict[str, Any],
    ) -> ToolResult:
        raise NotImplementedError

    @abstractmethod
    def list_definitions(self) -> list[ToolDefinition]:
        raise NotImplementedError