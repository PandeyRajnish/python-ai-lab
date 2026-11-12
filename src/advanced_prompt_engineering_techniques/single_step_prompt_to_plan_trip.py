from get_response import get_response

# Single-step prompt to plan a trip
# Imagine you're a developer taking a break and you want to apply your prompting skills to plan the perfect beach vacation. As an initial step, you decide to use a standard single-step prompt to seek assistance.


# The get_response() function in this exercise employs the max_tokens parameter to help this exercise run faster.

# Instructions
# Create a single-step prompt asking the model to help you plan a beach vacation.

# Create a single-step prompt to get help planning the vacation
prompt = """Help me to plan a beach vacation"""

response = get_response(prompt)
print(response)
