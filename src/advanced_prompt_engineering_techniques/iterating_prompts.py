from get_response import get_response

# Iterative prompt engineering for standard prompts
# You are a developer using prompt engineering techniques for your various tasks, and you want to carefully select the right language model. You wrote an initial prompt to know what are the top ten pre-trained language models out there. Now, your goal is to refine this prompt to generate a table presenting information on each model's name, release year and its owning company.

# Instructions
# Iteratively refine the prompt to get the desired outcome: a table with three columns for the top ten pre-trained language models, listing the model name, release year, and owning company.

# Refine the following prompt
prompt = """Give me the top 10 pre-trained language models. Present the results in a table with exactly three columns:
1. Model Name
2. Release Year
3. Owning Company"""

response = get_response(prompt)
print(response)
