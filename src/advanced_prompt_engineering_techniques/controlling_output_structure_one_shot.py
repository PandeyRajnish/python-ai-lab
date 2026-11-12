from get_response import get_response

# Controlling output structure
# One way to control the output structure provided by a language model is to give it a sample question-answer in the prompt. The model will learn from it and follow it when generating responses for similar questions. This exercise aims to let you build a one-shot prompt that extracts odd numbers from a given set of numbers and displays them as a set of numbers between brackets, separated by commas as shown in the instructions.

# Instructions
# Create a one-shot prompt that provides an example showing how to extract the odd numbers from the set {1, 3, 7, 12, 19}, and seeks an answer for the set {3, 5, 11, 12, 16}.

# Create a one-shot prompt
prompt = """Extract the odd numbers from the given set and return them inside the curly brackets, separated by commas.

Example:
Input: {1, 3, 7, 12, 19}
Output: {1, 3, 7, 19}

Now extract the odd numbers:
Input: {3, 5, 11, 12, 16}
Output:
"""

response = get_response(prompt)
print(response)
