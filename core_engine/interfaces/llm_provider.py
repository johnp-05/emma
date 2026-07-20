from abc import ABC, abstractmethod


class ILLMProvider(ABC):
    """Contrato para cualquier proveedor de modelos de lenguaje."""

    @abstractmethod
    async def generate_response(self, prompt: str) -> str:
        """Genera una respuesta a partir de un texto."""
        pass