import numpy as np

n,m=map(int,input().split())
arrint_a=[]
arrint_b=[]
for i in range(n):
    arrint_a.append(list(map(int,input().split())))
for i in range(n):
    arrint_b.append(list(map(int,input().split())))
print(np.add(arrint_a,arrint_b))
print(np.subtract(arrint_a,arrint_b))
print(np.multiply(arrint_a,arrint_b))
print(np.floor_divide(arrint_a,arrint_b))
print(np.mod(arrint_a,arrint_b))
print(np.power(arrint_a,arrint_b))
