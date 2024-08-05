#!/bin/python3

import math
import os
import random
import re
import sys

first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
cadfin=''
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
for j in range(m):
    for i in range(n):
        cadfin=cadfin+matrix[i][j]
print(cadfin)

cad="This$#is% Matrix#  %!"
regex=r"\w\W+\w"
#regex=r"\w[°!#%&/=¡¿;:,~\$\s]+\w"
#ocurrslst=[]
ocurrslst=re.findall(regex,cad)
cadret=''
lastpos=0
for i in range(len(ocurrslst)):
    elem=ocurrslst[i]
    print(elem)
    startelem=cad.find(elem)
    print(startelem)
    c2repl=elem[1:len(elem)-1]
    print(elem,"| ini:",elem[0],"| fin:",elem[len(elem)-1],"| 2repl:",c2repl)
    cad2=elem[0]+' '+elem[len(elem)-1]
    print(cad2)
    cadret=cadret+cad[lastpos:startelem]+cad2
    lastpos=startelem+len(elem)
cadret=cadret+cad[lastpos:]
print(cadret)