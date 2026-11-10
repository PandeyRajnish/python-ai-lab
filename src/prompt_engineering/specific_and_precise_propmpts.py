# Building specific and precise prompts
# In the previous exercise, you generated text that completes a given story. Your team was happy with your achievement, however, they want you to follow specific guidelines when it comes to length and style. Your task now is to craft a more specific prompt that controls these aspects of the generated story.

# The OpenAI package, the get_response() function, and the same story variable have been pre-loaded for you.

# Instructions
# Craft a prompt that completes the given story with only two paragraphs in the style of Shakespeare; use f-string, and delimit the story with triple backticks (```).

from get_response import get_response

story = "One rainy evening, Maya discovered a tiny door behind her bookshelf. A mysterious voice whispered her name from the darkness."

# Create a request to complete the story
prompt = f"""Complete the following story with only two paragraphs in the style of Shakespeare. The story is delimited by triple backticks.
```
{story}
```
"""

# Get the generated response
response = get_response(prompt)

print("\n Original story: \n", story)
print("\n Generated story: \n", response)
