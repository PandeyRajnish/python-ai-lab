from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {
            "role": "user",
            "content": "Write a polite reply accepting an AI Engineer job offer.",
        }
    ],
    max_completion_tokens=10,
)

print(response.choices[0].message.content)
