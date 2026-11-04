from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# Create a detailed prompt
prompt = """
Write a persuasive and engaging product description for SonicPro headphones.

Highlight the following key features:
1. Active Noise Cancellation (ANC) for an immersive listening experience.
2. Up to 40 hours of battery life for uninterrupted music.
3. Foldable design for easy storage and portability.

Use professional marketing language to attract potential customers.
Focus on product benefits, convenience, comfort, and premium audio quality.

Keep the description engaging, customer-focused, and suitable for an e-commerce website.
Include a catchy headline and a compelling call to action.
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    # Experiment with max_completion_tokens and temperature settings
    max_completion_tokens=400,
    temperature=0,
)

print(response.choices[0].message.content)
