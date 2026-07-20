import asyncio

from core_engine.events.event import Event
from core_engine.events.event_bus import EventBus
from core_engine.events.event_types import EventType


async def on_user_message(event: Event):

    print("📩 Evento recibido")
    print(f"Tipo: {event.type}")
    print(f"Mensaje: {event.payload}")


async def main():

    bus = EventBus()

    bus.subscribe(
        EventType.USER_MESSAGE,
        on_user_message
    )

    await bus.publish(
        Event(
            type=EventType.USER_MESSAGE,
            payload="Hola Emma"
        )
    )


if __name__ == "__main__":
    asyncio.run(main())