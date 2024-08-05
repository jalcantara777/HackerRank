import re
#s = 'jose anto hug' #input().rstrip().split()
#s= 'hello   world  lol'
#s='1 2 2 3 4 5 6 7 8  9'
#s='q w e r t y u i o p a s d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M'
s='132 456 Wq  m e'

news=re.sub('   ',' ##',s)
news=re.sub('  ',' #',news)

words=news.split()
fullname=''
cadret=''
for elem in words:
    start=elem.count('#')
    wchr1st=elem[start]
    if ((ord(wchr1st)>=97 and ord(wchr1st)<=122)):
        wchr1st=chr(ord(wchr1st)-32)
    if ord(wchr1st)==164:
        wchr1st=chr(165)
    capword=('#'*start)+wchr1st+elem[start+1:]
    fullname=fullname+capword+' '
fullname.rstrip()
cadret=re.sub('#',' ',fullname)
print(cadret)
