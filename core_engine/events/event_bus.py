from collections import defaultdict
from collections.abc import Awaitable, Callable

from core_engine.events.event import Event


EventHandler = Callable[[Event], Awaitable[None]]


class EventBus:
    """
    Bus de eventos asíncrono.
    Permite publicar eventos y notificar a todos los módulos suscritos.
    """

    def __init__(self) -> None:
        self._subscribers: dict[str, list[EventHandler]] = defaultdict(list)

    def subscribe(
        self,
        event_type: str,
        handler: EventHandler,
    ) -> None:
        """
        Registra un listener para un tipo de evento.
        """
        self._subscribers[event_type].append(handler)

    async def publish(
        self,
        event: Event,
    ) -> None:
        """
        Publica un evento y notifica a todos los listeners registrados.
        """
        handlers = self._subscribers.get(event.type, [])

        for handler in handlers:
            await handler(event)