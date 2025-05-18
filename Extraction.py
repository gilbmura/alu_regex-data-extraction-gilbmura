import re

# Sample strings
sample_text = """
Email: user@example.com, firstname.lastname@company.co.uk
URLs: https://www.example.com, https://subdomain.example.org/page
Phones: (123) 456-7890, 123-456-7890, 123.456.7890
Credit Cards: 1234 5678 9012 3456, 1234-5678-9012-3456
Times: 14:30, 2:30 PM
"""

# Regex patterns
patterns = {
    "emails": r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b",
    "urls": r"https?://[^\s]+",
    "phones": r"(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})",
    "credit_cards": r"(\d{4}[-\s]\d{4}[-\s]\d{4}[-\s]\d{4})",
    "times": r"\b(?:[01]?\d|2[0-3]):[0-5]\d\b|\b(?:1[0-2]|0?[1-9]):[0-5]\d\s?(?:AM|PM|am|pm)\b"
}

# Extract and display results
for key, pattern in patterns.items():
    print(f"--- {key.upper()} ---")
    matches = re.findall(pattern, sample_text)
    for match in matches:
        print(match)
    print("\n")
