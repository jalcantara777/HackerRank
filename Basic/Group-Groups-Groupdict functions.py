import re

m = re.match(r"\w*?([a-zA-Z0-9])\1+",input())
print(m.group(1) if m else -1)
