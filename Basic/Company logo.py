import math
import os
import random
import re
import sys

s='aabbbccde'
#s='google'
#s='qwertyuiopasdfghjklñzxcvbnm'
clave1,clave2,clave3='','',''
lstclv1=[]
lstclv2=[]
lstclv3=[]

letters=[]
for i in range(97,123):
    letters.append(chr(i))
result=dict.fromkeys(letters)
for i in range(26):
    result[letters[i]]=s.count(letters[i])
print(result)

lstvals=list(result.values())
maxval1=max(lstvals)
nummax1=lstvals.count(maxval1)
print('maxval1:',maxval1,' | num:',nummax1)

for clave,valor in result.items():
    if valor==maxval1:
        lstclv1.append(clave)

def orderlist(valtope,lst2ord):
    lst2ord.sort()
    for i in range(len(lst2ord)):
        if i<=(valtope-1):
            print(lst2ord[i],result[lst2ord[i]])

if nummax1==1:
    print(lstclv1[0], result[lstclv1[0]])
    # imprimir el 2° y 3° valor máx
    lstvals.remove(maxval1)
    maxval2=max(lstvals)
    nummax2=lstvals.count(maxval2)
    print('maxval2:',maxval2,' | num:',nummax2)

    for clave,valor in result.items():
        if valor==maxval2:
            lstclv2.append(clave)
    if nummax2==1:
        print(lstclv2[0], result[lstclv2[0]])

        # imprimir el 3° valor máx
        lstvals.remove(maxval2)
        maxval3=max(lstvals)
        nummax3=lstvals.count(maxval3)
        print('maxval3:',maxval3,' | num:',nummax3)

        for clave,valor in result.items():
            if valor==maxval3:
                lstclv3.append(clave)
        if nummax3==1:
            print(lstclv3[0], result[lstclv3[0]])
        else: #nummax3>1
            orderlist(1,lstclv3)

    else: #nummax2>1
        orderlist(2,lstclv2)

else: #nummax1=2,3
    orderlist(3,lstclv1)
    if nummax1==2:
        # imprimir el 2° valor max
        lstvals.remove(maxval1)
        lstvals.remove(maxval1)
        maxval2=max(lstvals)
        nummax2=lstvals.count(maxval2)
        #print('maxval2:',maxval2,' | num:',nummax2)

        for clave,valor in result.items():
            if valor==maxval2:
                lstclv2.append(clave)
        if nummax2==1:
            print(lstclv2[0], result[lstclv2[0]])
        else: #nummax2=2
            orderlist(1,lstclv2)
