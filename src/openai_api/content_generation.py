from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

prompt = """
Generate a catchy and memorable slogan for a new Italian restaurant.
The restaurant offers authentic Italian food, a cozy atmosphere,
and a premium dining experience.

Keep the slogan short, creative, and appealing to customers.
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens=20,
)

print(response.choices[0].message.content)
