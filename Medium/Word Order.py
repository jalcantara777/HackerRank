from collections import OrderedDict

summary = OrderedDict()
n=int(input())
for i in range(n):
  word=input()
  if word in summary:
      summary[word] += 1
  else:
      summary[word] = 1
print(len(summary.values()))
print(" ".join(map(str, summary.values()))) 
