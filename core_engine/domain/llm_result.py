from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True, slots=True)
class LLMResult:
    message: str
    tool_name: str | None = None
    tool_arguments: dict[str, Any] = field(default_factory=dict)

    @property
    def requires_tool(self) -> bool:
        return self.tool_name is not None