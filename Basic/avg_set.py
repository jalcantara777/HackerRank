n=10
arr=[161,182,161,154,176,170,167,171,170,174]

def average(array):
    # your code goes here
    sumval=0
    newlst=list(set(array))
    newn=len(newlst)
    for i in range(newn):
        sumval+=newlst[i]
    return (sumval/newn)

print(average(arr))