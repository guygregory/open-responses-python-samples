# Uses Server Side Events (SSE) to stream the response one line at a time
from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',  # required but ignored
)

stream = client.responses.create(
    model="phi4-reasoning",
    input="Write me a poem about the sea.",
    stream=True,
)

for event in stream:
    if event.type == 'response.output_text.delta':
        print(event.delta, end='')