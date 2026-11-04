from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

finance_text = """
The global financial market has experienced significant changes over the
past year due to inflation, interest rate adjustments, and economic uncertainty.

Many central banks have increased interest rates to control inflation.
As a result, borrowing costs have increased for businesses and individuals.
Stock markets have also experienced fluctuations as investors react to
economic reports and corporate earnings.

Despite these challenges, technology and renewable energy companies
continue to attract investments. Financial experts recommend that
investors diversify their portfolios, maintain emergency savings,
and focus on long-term investment strategies rather than short-term
market movements.
"""

# Use an f-string to format the prompt
prompt = f"""Summarize the following text into two concise bullet points:
{finance_text}"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens=30,
)

print(response.choices[0].message.content)
