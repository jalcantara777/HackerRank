from datetime import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    formato = "%a %d %b %Y %H:%M:%S %z"
    dttime1=datetime.strptime(t1,formato)
    dttime2=datetime.strptime(t2,formato)
    difftime=dttime1-dttime2
    return abs(int(difftime.total_seconds()))
    
if __name__ == '__main__':
    t = int(input())
    lst_delta=[]
    for t_itr in range(t):
        t1 = input()
        t2 = input()
        lst_delta.append(time_delta(t1, t2))
    for t_itr in range(t): print(lst_delta[t_itr])