n=int(input())
set_n = set(map(int, input().split()))
m=int(input())
for i in range(m):
  cmd_line=input()
  if cmd_line.count(' ')>0:
    set_oper,set_val=cmd_line.split()
  else:
    set_oper=cmd_line
  if set_oper== 'discard':
    set_n.discard(int(set_val))
  if set_oper== 'pop':
    set_n.pop()
  if set_oper== 'remove':
      if int(set_val) in set_n: set_n.remove(int(set_val))
print(sum(list(set_n)))