
from get_response import get_response

# Market research report summarization
# A market research firm needs to analyze and summarize lengthy reports on market trends and customer behavior. They want to know how AI and data privacy are shaping the market and how they're affecting customers. You are provided with a report string about markets trends and how they're affecting customer behavior. Your goal is to craft a prompt to summarize it while focusing on aspects related to AI and data privacy to see their effect on customers.

# Instructions
# Craft a prompt that summarizes the report (formatted using f-string) in maximum five sentences, while focusing on aspects related to AI and data privacy .

# Sample market research report (20 sentences, fictional scenario).
report = """Businesses are increasingly adopting artificial intelligence to understand customer preferences and improve their services.
Retailers use AI recommendation systems to suggest products based on browsing history and previous purchases.
These personalized recommendations can make shopping more convenient and encourage repeat purchases.
However, some customers feel uncomfortable when recommendations reveal how closely their activities are tracked.
AI chatbots help companies answer routine questions and provide support outside normal business hours.
Customers value quick responses but still prefer human assistance for complex or sensitive issues.
Marketing teams use predictive analytics to identify customer needs and tailor promotional campaigns.
The effectiveness of these campaigns depends on the quality and responsible use of customer data.
Data privacy has become an important consideration in how customers evaluate brands.
Customers want clear explanations of what information companies collect and why they need it.
Lengthy privacy notices and confusing consent options can weaken customer trust.
Simple privacy controls give customers more confidence when using digital services.
Some customers are willing to share limited personal information in exchange for useful personalized experiences.
Others prefer less personalization if it means reducing the amount of data collected about them.
Companies are exploring ways to improve AI services while collecting less personal information.
Businesses that explain their data practices clearly may build stronger customer relationships.
Security incidents can cause customers to stop using a service or switch to competing brands.
Customers also expect companies to explain when they are interacting with AI systems.
In this fictional market scenario, convenience, transparency, and control jointly influence purchasing decisions.
The report concludes that companies should balance AI-driven personalization with privacy protections to maintain customer trust."""

# Craft a prompt to summarize the report
prompt = f"""Summarize the market research report in maximum of five sentences. Focus specifically on how artificial intelligence (AI) and data privacy are shaping market trends and influencing customer behaviour.

Report: {report}
"""

response = get_response(prompt)

print("Summarized report: \n", response)
