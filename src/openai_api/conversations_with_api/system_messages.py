from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# System: controls assistant's behavior
# User: instruct the assistant
# Assistant: response to user instruction

response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_completion_tokens=50,
    messages=[
        {
            "role": "system",
            "content": "You are a study planning assistant that creates plans for learning new skills.",
        },
        {"role": "user", "content": "I want to learn to speak Japanease."},
    ],
)

print(response.choices[0].message.content)
