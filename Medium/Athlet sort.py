first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))
k = int(input().strip())

lst_ord=[]
for i in range(n):
    lst_ord.append(arr[i][k])
lst_ord.sort()
lst_ord2d=[]
for i in range(n):
    val2ord=lst_ord[i]
    for j in range(len(arr)):
        if arr[j][k]==val2ord:
            break
    lst_ord2d.append(arr.pop(j))
for i in range(len(lst_ord2d)):
    print(" ".join(map(str,lst_ord2d[i])))