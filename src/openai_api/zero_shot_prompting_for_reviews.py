from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

prompt = """
Classify the sentiment of each customer review using a number from 1 to 5.

Sentiment scale:
1 = Very positive
2 = Positive
3 = Neutral
4 = Negative
5 = Very negative

Classify each review:

1. Unbelievably good!
2. Shoes fell apart on the second use.
3. The shoes look nice, but they aren't very comfortable.
4. Can't wait to show them off!

Return only the review number and its sentiment score.
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens=100,
)

print(response.choices[0].message.content)
