import numpy as np

n,m,p=map(int,input().split())
arrint_n=[]
arrint_m=[]
for i in range(n):
   arrint_n.append(list(map(int,input().split())))
for i in range(m):
   arrint_m.append(list(map(int,input().split())))
print(np.concatenate((arrint_n,arrint_m)))