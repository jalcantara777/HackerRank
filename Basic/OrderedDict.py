from collections import OrderedDict

summary = OrderedDict()
n=int(input())
for i in range(n):
  cadentry=input()
  item, quantity = ' '.join(cadentry.split()[:-1]), int(cadentry.split()[-1])
  if item in summary:
      summary[item] += quantity
  else:
      summary[item] = quantity
for item, quantity in summary.items():
    print(f"{item} {quantity}")  
