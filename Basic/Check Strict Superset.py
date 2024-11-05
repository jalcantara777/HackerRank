# Check Superset
set_a = set(map(int, input().split()))
n=int(input())
issuperset=True
numelem_a=len(list(set_a))
for i in range(n):
  set_n = set(map(int, input().split()))
  issupersetn=True
  for elem in set_n:
    if not elem in set_a:
      issupersetn=False
      break
  issupersetn=(issupersetn and (numelem_a>len(list(set_n))))
  issuperset=(issuperset and issupersetn)
print('True' if issuperset else 'False')
  