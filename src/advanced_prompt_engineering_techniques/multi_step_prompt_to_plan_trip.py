from get_response import get_response

# Multi-step prompt to plan a trip
# You noticed that the single-step prompt was not effective, because the answer was too vague for what you had in mind. You improve your prompt by specifying the steps to follow for planning. The plan should have four potential locations for your beach vacation, and each location should have some accommodation options, some activities, and an evaluation of the pros and cons.

# The get_response() function in this exercise employs the max_tokens parameter to help this exercise run faster. This may truncate your solution.

# Instructions
# Create a multi-step prompt asking the model to make a plan for a beach vacation, which should include: four potential locations, each with some accommodation options, some activities, and an evaluation of the pros and cons.

# Create a prompt detailing steps to plan the trip
prompt = """Make a plan for a beach vacation by following these steps:
Step 1: Suggest four potential beach vacation locations.

Step 2: For each location, recommend some accommodation options.

Step 3: For each location, suggest activities to enjoy during the vacation.

Step 4: Evaulate the pros and cons of each location.

Present the results in a clear, organized format.
"""

response = get_response(prompt)
print(response)
