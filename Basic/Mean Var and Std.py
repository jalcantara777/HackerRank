import numpy as np

lst_main2d = []
n,m=input().split()
n=int(n)
m=int(m)
for i in range(n):
  lst_main2d.append(list(int(x) for x in input().split()))
my_array=np.array(lst_main2d)
print(np.mean(my_array,axis=1))
print(np.var(my_array,axis=0))
print(round(np.std(my_array),11))