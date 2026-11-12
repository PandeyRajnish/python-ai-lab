from get_response import get_response

# Reasoning with chain-of-thought prompts
# Chain-of-thought prompting is helpful to explain the reasoning behind the answer that the model is giving, especially in complex tasks such as generating the solution for a mathematical problem or a riddle. In this exercise, you will craft a chain-of-thought prompt to let the language model guess the age of your friend's father based on some information you will provide.


# Instructions
# Create a chain-of-thought prompt to determine your friend's father's age in 10 years, given that he is currently twice your friend's age, and your friend is 20.

# Create the chain-of-thought prompt
prompt = """Determine my friend's father's age in 10 years.
My friend is currently 20 years old, and his father is twice his age.
Think though the problem step by step and provide the final answer."""

response = get_response(prompt)
print(response)
