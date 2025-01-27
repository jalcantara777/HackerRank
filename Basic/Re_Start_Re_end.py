import re

text=input()
txt2find=input()
pattern = rf"(?=({txt2find}))"
matches = re.finditer(pattern, text)

found = False
for match in matches:
    found = True
    print((match.start(), match.end() + len(txt2find)-1))

if not found:
    print((-1, -1))