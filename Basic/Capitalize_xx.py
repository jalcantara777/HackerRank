import re

#s = 'jose anto hug' #input().rstrip().split()
s= 'hello   world  lol'

words=s.split()
fullname=''
cadret=''
for elem in words:
    wchr1st=elem[0]
    if ((ord(wchr1st)>=97 and ord(wchr1st)<=122)):
        wchr1st=chr(ord(wchr1st)-32)
    if ord(wchr1st)==164:
        wchr1st=chr(165)
    capword=wchr1st+elem[1:]
    fullname=fullname+capword+' '
fullname.rstrip()
num2spc=s.count('  ')
if num2spc>0:
    lastpos=0
    for i in range(1,num2spc+1):
        pos2spc=s.index('  ',lastpos)
        cadret=cadret+fullname[lastpos:pos2spc]+'  '
        lastpos=pos2spc+2
    cadret=cadret+fullname[lastpos-1:]
else:
    cadret=fullname
print(cadret)
