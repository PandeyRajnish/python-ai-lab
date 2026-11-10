# Exploring prompt engineering
# Prompt engineering refers to crafting effective prompts to guide the language model towards the intended response. By refining your prompts, you can achieve better results and guide the model towards generating more accurate and useful responses. Your task in this exercise is to modify the prompt you used in the previous exercise.

# The OpenAI package and the get_response() function have been pre-loaded for you.

# Instructions
# Craft a prompt that asks the model to generate a poem about ChatGPT while ensuring that it is written in basic English that a child can understand.
# Get the response using the get_response() function.

from get_response import get_response

prompt = "poem about chatgpt in basic English that a child can understand."

response = get_response(prompt)

print(response)
