# Check Subset
t=int(input())
for i in range(t):
  n=int(input())
  set_a = set(map(int, input().split()))
  m=int(input())
  set_b = set(map(int, input().split()))
  issubset=True
  for elem in set_a:
    if not elem in set_b:
      issubset=False
      break
  print('True' if issubset else 'False')
  