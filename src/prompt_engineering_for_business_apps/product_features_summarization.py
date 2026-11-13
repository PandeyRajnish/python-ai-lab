from get_response import get_response

# Product features summarization
# An electronics review website wants to provide concise and easy-to-read summaries of product features for its readers, allowing them to compare and evaluate different products quickly. The review website wants to generate bullet-point summaries, and, to start with, they want you to craft a prompt that summarizes a product_description for a smartphone.

# Instructions
# Craft a prompt that summarizes the product_description in no more than five bullet points.

# Sample product description (20 sentences about a fictional smartphone).
product_description = """The Nova X1 is a smartphone designed for everyday productivity, photography, and entertainment.
It features a 6.5-inch OLED display with a resolution of 2400 by 1080 pixels.
A 120 Hz refresh rate makes scrolling and animations look smooth.
The display supports HDR content for richer colors and improved contrast.
An octa-core processor powers applications and everyday multitasking.
The phone includes 8 GB of RAM and 256 GB of internal storage.
Storage can be expanded with a microSD card of up to 1 TB.
Its rear camera system combines a 50 MP main camera with a 12 MP ultrawide camera.
Optical image stabilization on the main camera helps reduce blur in photos and videos.
A dedicated night mode improves photos taken in low-light conditions.
The 16 MP front camera supports selfies and video calls.
The rear camera records video at up to 4K resolution at 30 frames per second.
A 5000 mAh battery is designed to support a full day of typical use.
The phone supports 45 W wired charging through its USB-C port.
It also supports 15 W wireless charging with a compatible charger.
Connectivity options include 5G, Wi-Fi 6, Bluetooth 5.3, and NFC.
An in-display fingerprint sensor provides convenient device unlocking.
An IP68 rating provides resistance to dust and water under specified test conditions.
The device runs Android and includes a commitment to four years of operating system updates.
The Nova X1 is available in Midnight Black and Ocean Blue, with a charging cable included in the box."""

# Craft a prompt to summarize the product description
prompt = f"""
Summarize the following smartphone product description in no more than five bullet points.
Focus on the key features and specifications.
Keep each bullet point concise, clear, and easy to understand.

Product Description:
{product_description}
"""

response = get_response(prompt)

print("Original description: \n", product_description)
print("Summarized description: \n", response)
