import numpy as np

n,m=input().split()
n=int(n)
m=int(m)
lst_numbers=[]
for i in range(n):
  lst_numbers.append(list(int(x) for x in input().split()))
print(np.transpose(lst_numbers))
print(np.array(lst_numbers).ravel())