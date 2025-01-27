import re

VOCALES = "aeiouAEIOU"
CONSONANTES = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
pattern = rf"(?<=[{CONSONANTES}])([{VOCALES}]{{2,}})(?=[{CONSONANTES}])"

result = re.findall(pattern, input())

if len(result) > 0:
    for i in range(len(result)): 
        print(result[i])
else:
    print(-1)
