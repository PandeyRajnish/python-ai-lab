from get_response import get_response

# Using delimited prompts with f-strings
# You are a junior developer at a dynamic startup that generates content with the help of AI. The company believes this technology can revolutionize storytelling, and you are excited to be a part of it. Today, your task is to generate a continuation of a story with a delimited prompt using an f-string.

# The OpenAI package, the get_response() function, and the story variable have been pre-loaded for you.

# Instructions
# Create a prompt asking to complete the variable story (provided to you as a string): use f-string, and delimit the story with triple backticks (```) to pass its content to the prompt.
# Get the generated response.

story = "One rainy evening, Maya discovered a tiny door behind her bookshelf. A mysterious voice whispered her name from the darkness."

# Create a prompt that completes the story
prompt = f"""Complete the story delimited by triple backticks.```{story}```"""

# Get the generated response
response = get_response(prompt)

print("\n Original story: \n", story)
print("\n Generated story: \n", response)
