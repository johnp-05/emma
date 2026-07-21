from abc import ABC, abstractmethod

from core_engine.domain.llm_result import LLMResult


class ILLMProvider(ABC):
    @abstractmethod
    async def generate_response(
        self,
        user_message: str,
    ) -> LLMResult:
        raise NotImplementedError