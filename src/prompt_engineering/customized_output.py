from get_response import get_response

text = """Every morning, Aisha cycles to the community garden before work.
Together with her neighbors, she grows fresh vegetables and shares the harvest
with local families. What began as a small weekend project has transformed an
empty lot into a welcoming space where friendships and healthy food flourish."""

# Customizing output format
# You work as a developer at a startup that offers a text analysis platform for content creators. Your platform helps users automatically categorize and format their content, and you're now working on a new feature that detects the language of a given piece of text and generates a suitable title for that text in a custom format. You decide to craft a prompt that guides the language model through this.

# Instructions
# Create the instructions for the prompt, asking the model to determine the language and generate a suitable title for the pre-loaded text excerpt that will be provided using triple backticks (```) delimiters.
# Create the output_format with directions to include the text, language, and title, each on a separate line, using 'Text:', 'Language:', and 'Title:' as prefixes for each line.
# Create the final_prompt by combining all parts and the delimited text to use.

# Create the instructions
instructions = "Determine the language and generate a suitable title for the text delimied by triple backticks."

# Create the output format
output_format = """Use the following format for the output:
- Text: <original text>
- Language: <detected language>
- Title: <generated title>"""

# Create the final prompt
final_prompt = instructions + "\n" + output_format + f"\n```{text}```"
response = get_response(final_prompt)
print(response)
