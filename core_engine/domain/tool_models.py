from dataclasses import dataclass, field
from typing import Any


@dataclass(frozen=True, slots=True)
class ToolDefinition:
    name: str
    description: str
    parameters: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class ToolResult:
    success: bool
    message: str
    data: Any | None = None
    error: str | None = None