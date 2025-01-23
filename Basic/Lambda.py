cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    i=0
    lst2ret=[]
    while i<n:
        if i==0:
            lst2ret.append(0)
        elif i==1:
            lst2ret.append(1)
        else:
            lst2ret.append(lst2ret[i-1]+lst2ret[i-2])
        i+=1
    return lst2ret

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))