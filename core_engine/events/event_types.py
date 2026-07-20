from enum import StrEnum


class EventType(StrEnum):
    USER_MESSAGE = "USER_MESSAGE"
    AI_RESPONSE = "AI_RESPONSE"
    SYSTEM_MESSAGE = "SYSTEM_MESSAGE"