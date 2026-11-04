from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# More assistant messages!
# Expand on your previous messages to provide additional examples, stored as example1, response1, example2, response2, example3, and response3.

# Let's see if we can get this model outputting information in the desired format!

# Instructions
# Expand your previous messages to include additional examples of other countries, which are stored as example1, response1, example2, response2, example3, and response3.

# Example variables
example1 = "Give me a quick summary of France."
response1 = "France is a country in Western Europe. Its capital city is Paris."

example2 = "Give me a quick summary of Japan."
response2 = "Japan is an island country in East Asia. Its capital city is Tokyo."

example3 = "Give me a quick summary of India."
response3 = "India is a country in South Asia. Its capital city is New Delhi."


response = client.chat.completions.create(
    model="gpt-4o-mini",
    # Add a user and assistant message for in-context learning
    messages=[
        {
            "role": "system",
            "content": "You are a helpful Geography tutor that generates concise summaries for different countries.",
        },
        {"role": "user", "content": "Give me a quick summary of Portugal."},
        {
            "role": "assistant",
            "content": "Portugal is a country in Europe that borders Spain. The capital city is Lisboa.",
        },
        {"role": "user", "content": example1},
        {"role": "assistant", "content": response1},
        {"role": "user", "content": example2},
        {"role": "assistant", "content": response2},
        {"role": "user", "content": example3},
        {"role": "assistant", "content": response3},
        {"role": "user", "content": "Give me a quick summary of Greece."},
    ],
)


print(response.choices[0].message.content)
