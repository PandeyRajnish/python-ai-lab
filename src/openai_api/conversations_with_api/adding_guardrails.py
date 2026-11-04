from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

sys_msg = """You are a study planning assistant that creates plans for learning new skills.

If these skills are non related to languages, return the message:

'Apologies, to focus on languages, we no longer create learning plans on other topics.'
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    max_completion_tokens=50,
    messages=[
        {"role": "system", "content": sys_msg},
        {"role": "user", "content": "Help me learn to DummyLanguage"},
    ],
)


print(response.choices[0].message.content)
