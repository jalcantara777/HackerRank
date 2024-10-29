from collections import deque

dq = deque()
n=int(input())
for i in range(n):
  cmd_line=input()
  if cmd_line.count(' ')>0:
    dq_oper,dq_val=cmd_line.split()
  else:
    dq_oper=cmd_line
  if dq_oper== 'append':
    dq.append(dq_val)
  if dq_oper== 'pop':
    dq.pop()
  if dq_oper== 'popleft':
    dq.popleft()
  if dq_oper== 'appendleft':
      dq.appendleft(dq_val)
print(" ".join(map(str, dq))) 
