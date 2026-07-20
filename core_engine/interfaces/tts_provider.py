from abc import ABC, abstractmethod


class ITTSProvider(ABC):
    """Contrato para proveedores de Texto a Voz."""

    @abstractmethod
    async def speak(self, text: str) -> None:
        """Reproduce un texto mediante voz."""
        pass