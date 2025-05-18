import re

sample_text = """
US: $19.99, $1,234.56, $1000000.00
EU: €19,99, €1.234,56, €1000000,00
Invalid: €1,000.000,00
"""

# This pattern ensures correct formatting for either US or EU styles but avoids mixed formats like "€1,000.000,00"
pattern = r"(?:[€$](?:\d{1,3}(?:,\d{3})*(?:\.\d{2})?|\d+(?:\.\d{2})?)|€(?:\d{1,3}(?:\.\d{3})*(?:,\d{2})?|\d+(?:,\d{2})?))"

matches = re.findall(pattern, sample_text)
print("--- MATCHED CURRENCY AMOUNTS ---")
for match in matches:
    print(match)
