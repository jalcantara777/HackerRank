#!/bin/python3
"""
x = int(input())
y = int(input())
z = int(input())
n = int(input())
"""

x=int(1)
y=int(1)
z=int(1)
n=int(2)

permut=[]
result=[]

for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            permut.append([i,j,k])

print(permut)
sumelem=int(0)

for elem in permut:
    sumelem=elem[0]+elem[1]+elem[2]
    print(elem,sumelem)
    if sumelem!=n:
        result.append(elem)

print(result)