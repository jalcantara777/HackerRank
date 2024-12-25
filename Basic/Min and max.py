import numpy as np

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

lst_ordkey = []
for _ in range(n):
    lst_ordkey.append(list(map(int, input().rstrip().split())))
print(np.max(np.min(lst_ordkey,axis=1)))