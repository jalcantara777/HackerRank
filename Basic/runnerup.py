n=5
arr=[2,3,6,6,5]

arr.sort(reverse=True)
maxval=max(arr)
for elem in arr:
    if elem<maxval:
        break
print(elem)
    


