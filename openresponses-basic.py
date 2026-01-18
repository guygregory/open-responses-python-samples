from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',  # required but ignored
)

responses_result = client.responses.create(
  model="gpt-oss:20b",
  input='Write a short poem about the color blue',
)
print(responses_result.output_text)