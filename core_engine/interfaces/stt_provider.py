from abc import ABC, abstractmethod


class ISTTProvider(ABC):
    """Contrato para proveedores de Voz a Texto."""

    @abstractmethod
    async def listen(self) -> str:
        """Escucha el micrófono y devuelve el texto reconocido."""
        pass