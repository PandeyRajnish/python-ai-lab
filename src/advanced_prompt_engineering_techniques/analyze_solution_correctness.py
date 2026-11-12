from get_response import get_response

# Analyze solution correctness
# You're back from your relaxing vacation and you've been assigned the task of reviewing and correcting some programming tasks, including a function to calculate of the area of a shape. You are provided with a code string that contains the function to calculate the area of a rectangle, and need to assess its correctness. The ideal function for you is a function that has correct syntax, receives two inputs, and returns one output.

# Instructions
# Create a multi-step prompt asking the model to assess the function provided in the delimited code string according to the three criteria: correct syntax, receiving two inputs, and returning one output.

code = """
def calculate_rectangle_area(length, width):
    area = length * width
    return area
"""

# Create a prompt that analyzes correctness of the code
prompt = """Determine the correctness of the code delimited by triple backtics as follows:
Step 1: Check if the code has correct Python syntax.
Step 2: Verify if the function receives exactly two inputs.
Step 3: Verify if the fucntion returns exactly one output.
Code: ```{code}```
"""

response = get_response(prompt)
print(response)
