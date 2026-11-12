from get_response import get_response

text = """Every morning, Aisha cycles to the community garden before work.
Together with her neighbors, she grows fresh vegetables and shares the harvest
with local families. What began as a small weekend project has transformed an
empty lot into a welcoming space where friendships and healthy food flourish."""

# Create the instructions
instructions = """Infer the language and count the number of sentence in the text delimited by triple backtics. If the tex contains more than one sentence, generate a suitable title. Otherwise, write 'N/A' for the title"""

# Create the output format
output_format = """Return the text, language, number of sentences, and title, each on a separate line, using this format:
Text: <original text>
Language: <detected language>
Number of sentences: <sentence count>
Title: <generated title or N/A>
"""

prompt = instructions + output_format + f"```{text}```"
response = get_response(prompt)
print(response)
