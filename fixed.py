import re

sample_text = """
US: $19.99, $1,234.56, $1000000.00
EU: €19,99, €1.234,56, €1.000.000,00
Invalid: €1,000.000,00
Emails: user@example.com, firstname.lastname@company.co.uk
Phones: (123) 456-7890, 123-456-7890, 123.456.7890
"""

# Currency pattern (US & EU, valid formats only)
currency_pattern = r"(?:[€$](?:\d{1,3}(?:,\d{3})*(?:\.\d{2})?|\d+(?:\.\d{2})?)|€(?:\d{1,3}(?:\.\d{3})*(?:,\d{2})?|\d+(?:,\d{2})?))"

# Email pattern
email_pattern = r"[\w.+-]+@[\w-]+\.[\w.-]+"

# Phone number pattern
phone_pattern = r"(?:\(\d{3}\) \d{3}-\d{4}|\d{3}[-.]\d{3}[-.]\d{4})"

# Find matches
currency_matches = re.findall(currency_pattern, sample_text)
email_matches = re.findall(email_pattern, sample_text)
phone_matches = re.findall(phone_pattern, sample_text)

# Output
print("--- MATCHED CURRENCY AMOUNTS ---")
for match in currency_matches:
    print(match)

print("\n--- MATCHED EMAIL ADDRESSES ---")
for match in email_matches:
    print(match)

print("\n--- MATCHED PHONE NUMBERS ---")
for match in phone_matches:
    print(match)
