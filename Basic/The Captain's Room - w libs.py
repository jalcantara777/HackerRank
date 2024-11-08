## The Captain's Room - w/ libs

from collections import Counter

k=int(input())
lst_allrooms = list(map(int, input().split()))
lst_roomscnt = Counter(lst_allrooms)
for elem in Counter(lst_allrooms).items():
  if elem[1]==1: break
print(elem[0])