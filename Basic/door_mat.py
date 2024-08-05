n=int(input())
m=n*3

"""
#ANOTHER INPUT WAY: '%d %d'
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])
"""

center =int((n-1)/2+1)
txtfin=''

def fillrowup(num):
    minus=int((m-3)/2)
    txt='-'*(minus-3*(num-1))+'.'+'|..'*(num-1)+'|'+'..|'*(num-1)+'.'+'-'*(minus-3*(num-1))
    return txt

for i in range(1,n+1):
    if i<center:
        txtfin=txtfin+fillrowup(i)+'\n'
    elif i==center:
        txtfin=txtfin+'-'*int((m-7)/2)+'WELCOME'+'-'*int((m-7)/2)+'\n'
    else:
         txtfin=txtfin+fillrowup(n-i+1)+'\n'

print(txtfin)