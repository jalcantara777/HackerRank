T=int(input())
lst_tcases=[]
for i in range(T):
  n=int(input())
  lst_tcases.append(list(int(x) for x in input().split()))

for i in range(T):
  lstpiled=[]
  lst2pile=lst_tcases[i]
  n=len(lst2pile)
  for j in range(n-1,0,-1):
    max_val=max(lst2pile[0],lst2pile[j])
    lastval=(lstpiled[n-j-2] if j<n-1 else 2**31)
    if max_val<=lastval:
      yon='Yes'
      lstpiled.append(max_val)
      if lst2pile[0]==max_val:
        lst2pile.pop(0)
      else:
        lst2pile.pop()
    else:
      yon='No'
      break
  print(yon)