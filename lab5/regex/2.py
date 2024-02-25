import re

file=open("row.txt", "r", encoding="utf8")
text= file.read()

if re.search('a(b{2-3})', text):
    print("matches")
else:
    print("no matches")