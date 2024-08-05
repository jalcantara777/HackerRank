
import statistics
n = 3
student_marks = {'Krishna':[67,68,69],'Arjun':[70,98,63],'Malika':[52,56,60]}
query_name = 'Malika'
"""
n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
"""
lstkeys=student_marks.keys()
lst2avg=[]
for elem in lstkeys:
    if elem==query_name:
        lst2avg=student_marks[elem]
print(f'{statistics.mean(lst2avg):.2f}')
