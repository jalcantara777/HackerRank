n=5
lstvals=[['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
lstscor=[]
"""
lstvals=[]
for _ in range(int(input())):
    name = input()
    score = float(input())
    lstname.append(name)
    lstscor.append(score)
    lstvals.append([name,score])
"""
for elem in lstvals:
    lstscor.append(elem[1])

lstscor.sort()
minval=min(lstscor)
for elem in lstscor:
    if elem>minval:
        break
min2nd=elem
lstret=[]
for elem in lstvals:
    if elem[1]==min2nd:
        lstret.append(elem[0])
lstret.sort()
for elem in lstret:
    print(elem)   