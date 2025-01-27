import numpy as np

n,m=map(int,input().split())
my_arrint=[]
for i in range(n):
   my_arrint.append(list(map(int,input().split())))
my_arrint=np.array(my_arrint)
print(np.prod(np.sum(my_arrint,axis=0)))