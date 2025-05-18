import re

sample_text = """
Emails: us@er@example.com, firstname.lastname@company.co.uk, 
         invalid-email@.com, @missing@username.com, user999@domain..com
"""
email_pattern = r"(?!.*@.*@)[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}"

email_matches = re.findall(email_pattern, sample_text)

print("\n--- MATCHED EMAIL ADDRESSES ---")
for match in email_matches:
    print(match)