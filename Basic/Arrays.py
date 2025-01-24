import numpy

def arrays(arr):
    arr2=list(arr[i] for i in range(len(arr)-1,-1,-1))
    return numpy.array(arr2, float)
    # complete this function
    # use numpy.array

arr = input().strip().split(' ')
result = arrays(arr)
print(result)