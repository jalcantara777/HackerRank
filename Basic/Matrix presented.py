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

regex=r"\w\W+\w"
ocurrslst=re.findall(regex,cadfin)
cadret=''
lastpos=0
for i in range(len(ocurrslst)):
    elem=ocurrslst[i]
    startelem=cadfin.find(elem)
    c2repl=elem[1:len(elem)-1]
    cad2=elem[0]+' '+elem[len(elem)-1]
    cadret=cadret+cadfin[lastpos:startelem]+cad2
    lastpos=startelem+len(elem)
cadret=cadret+cadfin[lastpos:]
print(cadret)