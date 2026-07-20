from core_engine.contracts.tools import ITool


class ToolRegistry:
    def __init__(self) -> None:
        self._tools: dict[str, ITool] = {}

    def register(self, tool: ITool) -> None:
        name = tool.definition.name

        if name in self._tools:
            raise ValueError(f"Tool '{name}' ya está registrada.")

        self._tools[name] = tool

    def get(self, name: str) -> ITool:
        try:
            return self._tools[name]
        except KeyError as exc:
            raise ValueError(f"Tool '{name}' no encontrada.") from exc

    def exists(self, name: str) -> bool:
        return name in self._tools

    def all(self) -> list[ITool]:
        return list(self._tools.values())