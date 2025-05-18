import re

sample_text = """
<p>This is a paragraph.</p>
<div class="example">Div content</div>
<img src="image.jpg" alt="description">
"""

# Regex for HTML tags
pattern = r"<[^>]+>"

matches = re.findall(pattern, sample_text)
print("--- HTML TAGS ---")
for match in matches:
    print(match)
