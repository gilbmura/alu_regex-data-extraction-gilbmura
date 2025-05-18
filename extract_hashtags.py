import re

sample_text = """
#example is a sample hashtag
We are using #ThisIsAHashtag in our campaign!
#Hashtags are great for social media#and marketing.
"""

# Regex for hashtags
pattern = r"#\w+"

matches = re.findall(pattern, sample_text)
print("--- HASHTAGS ---")
for match in matches:
    print(match)
