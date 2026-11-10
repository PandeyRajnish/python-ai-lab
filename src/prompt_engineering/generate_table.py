from get_response import get_response

# Generating a table
# Imagine you are a developer working for a renowned online bookstore known for its extensive collection of science fiction novels. Today, you have a task at hand: to create a table of ten must-read science fiction books for the website's homepage. This will enhance the user experience on the website, helping fellow sci-fi enthusiasts discover their next great read.

# The OpenAI package and the get_response() function have been pre-loaded for you.

# Instructions
# Craft a prompt that generates a table of 10 books, with columns for Title, Author, and Year, that you should read given that you are a science fiction lover.
# Get the response.

# Create a prompt that generates the table
prompt = "Generate a table containing 10 books I should read if I am a science fiction lover. Include the columns Title, Author, and Year."

# Get the response
response = get_response(prompt)
print(response)
