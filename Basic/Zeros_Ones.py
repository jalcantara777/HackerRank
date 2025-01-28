import numpy as np

lst_vals=list(map(int,input().split()))
m=lst_vals[1]
n=lst_vals[0]
if len(lst_vals)>2: 
  if len(lst_vals)==3: 
    p=lst_vals[2]
    print(np.zeros((n,m,p), dtype = int))
    print(np.ones((n,m,p), dtype = int))
  else:
    p=lst_vals[2]
    q=lst_vals[3]
    print(np.zeros((n,m,p,q), dtype = int))
    print(np.ones((n,m,p,q), dtype = int))
else:
  print(np.zeros((n,m), dtype = int))
  print(np.ones((n,m), dtype = int))