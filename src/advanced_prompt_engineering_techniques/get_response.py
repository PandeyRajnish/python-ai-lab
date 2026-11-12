from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


def get_response(prompt):
    # Create a request to the chat completions endpoint
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        max_completion_tokens=100,
    )
    return response.choices[0].message.content


# Test the function with your prompt
# response = get_response("Which one is the latest thinking model?")

# print(response)