from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# Creating the get_response() function
# Most of the exercises in this course will call the chat.completions endpoint of the OpenAI API with a user prompt. Here, you will create a get_response() function that receives a prompt as input and returns the response as an output, which in future exercises will be pre-loaded for you.


# Instructions
# Create a request to the chat.completions endpoint inside the get_response() function.
# Try out the function with a prompt that asks the model to write a poem about ChatGPT.


def get_response(prompt):
    # Create a request to the chat completions endpoint
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
    )
    return response.choices[0].message.content


# Test the function with your prompt
response = get_response("Which one is the latest thinking model?")

print(response)