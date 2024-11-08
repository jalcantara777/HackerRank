## The Captain's Room
k=int(input())
lst_rooms = list(map(int, input().split()))
set_n=set(lst_rooms)
for elem in set_n:
  if lst_rooms.count(elem)==1: break
print(elem)