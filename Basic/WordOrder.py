n=4
lwords=['avg','abc','cat','avg']

def setunord(lst):
    lstret=[]
    lstret.append(lst[0])
    for i in range(1,len(lst)):
        if (lstret.count(lst[i])==0):
            lstret.append(lst[i])
    return lstret
"""
n=int(input())
lwords=[]
for i in range(n):
    w=input()
    lwords.append(w)
"""

lsetw=setunord(lwords)
print(len(lsetw))
cadret=''
for elem in lsetw:
    cadret=cadret+str(lwords.count(elem))+' '
print(cadret)