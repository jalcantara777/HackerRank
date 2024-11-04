n,m=input().split()
n=int(n)
m=int(m)
lst_vals=list(int(x) for x in input().split())
set_a=list(int(x) for x in input().split())
set_b=list(int(x) for x in input().split())
hapiness=0
for elem in lst_vals:
  if set_a.count(elem)>0: 
    hapiness+=1
  elif set_b.count(elem)>0: 
    hapiness-=1
print(hapiness)