## Set Mutations
x=int(input())
set_a = set(map(int, input().split()))
n=int(input())
for i in range(n):
  set_oper,set_val=input().split()
  set_n = set(map(int, input().split()))
  if set_oper== 'update':
    set_a.update(set_n)
  if set_oper== 'intersection_update':
    set_a.intersection_update(set_n)
  if set_oper== 'difference_update':
    set_a.difference_update(set_n)
  if set_oper== 'symmetric_difference_update':
    set_a.symmetric_difference_update(set_n)
print(sum(list(set_a)))
