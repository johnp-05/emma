import asyncio

from core_engine.core.emma_core import EmmaCore
from core_engine.providers.mocks.mock_llm import MockLLMProvider
from core_engine.providers.mocks.mock_stt import MockSTTProvider
from core_engine.providers.mocks.mock_tts import MockTTSProvider


async def main():

    emma = EmmaCore(
        llm_provider=MockLLMProvider(),
        stt_provider=MockSTTProvider(),
        tts_provider=MockTTSProvider(),
    )

    await emma.process_interaction()


if __name__ == "__main__":
    asyncio.run(main())