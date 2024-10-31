x,k=input().split()
x=int(x)
k=int(k)
p=input()
vnp=0
exec('vnp='+p.replace('x',str(x)))
print('True' if vnp==k else 'False')
