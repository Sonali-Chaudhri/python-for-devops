import re

text = "The quick brown fox"
pattern = r"brown"

search = re.search(pattern, text)
if search:
    print("Pattern found:", search.group())
else:
    print("Pattern not found")


text="i am sonali"
pattern=r"brown"
search=re.search(pattern,text)
if search:
    print("pattern found",search.group())
else:
    print("pattern not found")