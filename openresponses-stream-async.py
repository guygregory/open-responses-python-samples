# Uses async client to continuously stream data from the server to the client.
from openai import AsyncOpenAI
import asyncio

client = AsyncOpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',  # required but ignored
)

async def main():
    stream = await client.responses.create(
        model="gpt-oss:20b",
        input="Write me a poem about the sea.",
        stream=True,
    )

    async for event in stream:
        if hasattr(event, "delta") and event.delta:
            print(event.delta, end="", flush=True)

asyncio.run(main())
