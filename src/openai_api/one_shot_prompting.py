from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# Add the example to the prompt
prompt = """Classify sentiment as 1-5 (negative to positive):
1. Love these! = 5
2. Unbelievably good! =
3. Shoes fell apart on the second use. =
4. The shoes look nice, but they aren't very comfortable. =
5. Can't wait to show them off! ="""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens=100,
)

print(response.choices[0].message.content)
