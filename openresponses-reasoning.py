from openai import OpenAI

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',  # required but ignored
)

response = client.responses.create(
    model="gpt-oss:20b",
    input="How much wood would a woodchuck chuck?",
    reasoning={
        "effort": "medium",
        "summary": "auto",
    }
)

# Extract and print reasoning summary (Optional)
reasoning_summaries = []

for item in response.output:
    if getattr(item, "type", None) == "reasoning":
        for part in (item.summary or []):
            if getattr(part, "type", None) == "summary_text":
                reasoning_summaries.append(part.text)

print("=== Reasoning summary ===")
print("\n\n".join(reasoning_summaries) if reasoning_summaries else "(none)")

# Print results
print("\n=== Final answer ===")
print(response.output_text)