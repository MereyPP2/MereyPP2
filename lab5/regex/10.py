import re
file = open("row.txt", "r", encoding="utf8")
text = file.read()
x = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', text).lower()
print(x)