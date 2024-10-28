from collections import defaultdict

d = defaultdict(list)
n,m=input().split()
n=int(n)
m=int(m)

# to read values
for i in range(n):
  d['GroupA'].append(input())
for i in range(m):
  d['GroupB'].append(input())

# to check and count GroupB values
for j in range(m):
  if  d['GroupA'].count(d['GroupB'][j])>0:
    indexes= [i+1 for i, x in enumerate(d['GroupA']) if x == d['GroupB'][j]]
    val_return=" ".join(map(str, indexes))
  else:
    val_return='-1'
  print(val_return)