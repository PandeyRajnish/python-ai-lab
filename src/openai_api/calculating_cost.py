from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

prompt = """Replace car with plane and adjust phrase:
A car is a vehicle that is typically powered by an internal combustion engine or an electric motor. It has four wheels, and is designed to carry passengers and/or cargo on roads or highways. Cars have become a ubiquitous part of modern society, and are used for a wide variety of purposes, such as commuting, travel, and transportation of goods. Cars are often associated with freedom, independence, and mobility."""

max_completion_tokens = 30

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens=max_completion_tokens,
)

input_token_price = 0.15 / 1_000_000
output_token_price = 0.6 / 1_000_000

# extract token usage
input_tokens = response.usage.prompt_tokens
output_tokens = response.usage.completion_tokens

# calculate cost
cost = input_tokens * input_token_price + output_tokens * output_token_price

# print response
print(f"Input tokens: {input_tokens}")
print(f"Output tokens: {output_tokens}")
print(f"Total tokens: {response.usage.total_tokens}")
print(f"Estimated cost: ${cost:.8f}")
