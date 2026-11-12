from get_response import get_response

# Self-consistency prompts
# Imagine you own a store that sells laptops and mobile phones. You start your day with 50 devices in the store, out of which 60% are mobile phones. Throughout the day, three clients visited the store, each of them bought one mobile phone, and one of them bought additionally a laptop. Also, you added to your collection 10 laptops and 5 mobile phones. How many laptops and mobile phones do you have by the end of the day? This problem is defined in the problem_to_solve string, and you will use a self-consistency prompt to solve it.

# The get_response() function in this exercise employs the max_tokens parameter to help this exercise run faster.

# Instructions
# Create the self_consistency_instruction that allows the model to solve the problem with three experts and combine the results with a majority vote.
# Create the final prompt by combining the self_consistency_instruction and the problem_to_solve.

# Create the self_consistency instruction
self_consistency_instruction = """Imagine three independent experts solving the following problem. Each Expert should solve the problem independently, showing their calculations. Compare the three answers and use a majority vote to determine the final answer."""

# Create the problem to solve
problem_to_solve = "If you own a store that sells laptops and mobile phones. You start your day with 50 devices in the store, out of which 60% are mobile phones. Throughout the day, three clients visited the store, each of them bought one mobile phone, and one of them bought additionally a laptop. Also, you added to your collection 10 laptops and 5 mobile phones. How many laptops and mobile phones do you have by the end of the day?"

# Create the final prompt
prompt = self_consistency_instruction + "\n\n" + problem_to_solve

response = get_response(prompt)
print(response)
