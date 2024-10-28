from collections import namedtuple

n=int(input())
tot=0
Students=namedtuple('Students',input())
for i in range(n): 
  a,b,c,d=input().split()
  stu_dta=Students(a,b,c,d)
  tot +=int(stu_dta.MARKS)
print(tot/n)