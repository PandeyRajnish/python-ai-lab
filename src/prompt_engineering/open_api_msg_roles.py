from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# OpenAI API message roles
# You are developing a chatbot for an event management agency that will be used to facilitate networking during events.

# Using the OpenAI API, you prepare a dictionary to pass as the message to the chat.completions endpoint. The message needs to have 3 roles defined to ensure the model has enough guidance to provide helpful responses.

# Throughout the course, you'll write Python code to interact with the OpenAI API. Entering your own API key is not necessary to create requests and complete the exercises in this course. You can leave the placeholder "<OPENAI_API_TOKEN>" as the key in api_key.

# The OpenAI package has been pre-loaded for you.

# Instructions
# Create an OpenAI API Python client; setting your personal key is not required, you can leave the placeholder.
# Complete the dictionary of messages with the role corresponding to each of the messages provided.

conversation_messages = [
    {"role": "system", "content": "You are a helpful event management assistant."},
    {
        "role": "user",
        "content": "What are some good conversation starters at networking events?",
    },
    {"role": "assistant", "content": ""},
]

response = client.chat.completions.create(
    model="gpt-4o-mini", messages=conversation_messages
)

print(response.choices[0].message.content)
