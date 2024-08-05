n=4
lwords=['avg','abc','cat','avg']

"""
for _ in range(int(input())):
    lwords=input().split('\n')
"""
lstret=[]
cadret=''
for i in range(len(lwords)):
    word=lwords[i]
    if (lstret.count(word)==0):
        lstret.append(word)
        cadret=cadret+str(lwords.count(word))+' '

print(len(lstret))
print(cadret)