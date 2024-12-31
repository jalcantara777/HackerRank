import re

pattern = r"^[-+]?\d*\.\d+$"

T=int(input())
for i in range(T):
    if re.fullmatch(pattern, input()):
        print("True")
    else:
        print("False")