import re

VOCALES = "aeiou"
CONSONANTES = "bcdfghjklmnpqrstvwxyz"
pattern = rf"[{VOCALES}]([{CONSONANTES}])\1+[{VOCALES}]"
matches = re.finditer(pattern, input())

# Extraemos las subcadenas completas que contienen las consonantes repetidas
result = [match.group(0)[1:-1] for match in matches]

if len(result) > 0:
    for i in range(len(result)): print(result[i])
else:
    print(-1)