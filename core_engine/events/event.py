from dataclasses import dataclass, field
from datetime import datetime
from typing import Any
from uuid import uuid4


@dataclass(slots=True)
class Event:
    """
    Representa un evento intercambiado entre los módulos de Emma.
    """

    type: str
    payload: Any = None

    id: str = field(default_factory=lambda: str(uuid4()))
    timestamp: datetime = field(default_factory=datetime.utcnow)