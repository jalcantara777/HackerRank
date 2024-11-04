import numpy as np

n=int(input())
A=[]
for i in range(n):
  A.append(list(int(x) for x in input().split()))
B=[]
for i in range(n):
  B.append(list(int(x) for x in input().split()))
print(np.dot(A,B))