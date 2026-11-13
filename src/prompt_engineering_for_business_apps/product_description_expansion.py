from get_response import get_response

# Product description expansion
# As you continue your work on the electronics review website, you've come across some products that are already summarized but lack a comprehensive description. Your task now is to expand these concise product descriptions into detailed narratives, ensuring that each product has both a full description and a bulleted summary for easy comparison. The complete description should effectively capture the product's unique features, benefits, and potential applications. You will apply your first prompt on a smart home security camera's product description.

# Instructions
# Craft a prompt that expands the product_description pre-loaded string, and writes a one paragraph comprehensive overview capturing the key information of the product: unique features, benefits, and potential applications.

# Short sample description of a fictional product.
product_description = """The HomeGuard Mini is an indoor smart security camera with 1080p video, night vision, and motion detection alerts. Two-way audio lets you talk to family members or pets through a mobile app. It connects to Wi-Fi and supports local microSD storage for monitoring entrances, living rooms, or pet areas."""

# Craft a prompt to expand the product's description
prompt = f"""Expand the following smart home security camera product description into the comprehensive paragraph.

Highlight the product's unique features, benefits, and potential applications. Provide a detailed, clear, and engagin overview while maintaining accuracy.

Product Description:
{product_description}
"""

response = get_response(prompt)

print("Original description: \n", product_description)
print("Expanded description: \n", response)
