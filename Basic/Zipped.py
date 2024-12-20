N,X=input().split()
N=int(N)
X=int(X)
lst_allmrks=[]
for i in range(X):
  lst_allmrks.append(list(map(float, input().split())))
lst_x=list(zip(*lst_allmrks))
for i in range(N): print(sum(lst_x[i])/X)