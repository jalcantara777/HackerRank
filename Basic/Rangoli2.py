size=5

def solve(size):
    cols=1
    abc=[]
    for k in range(97,123):
        abc.append(chr(k))
    if size==1:
        return 'a\n'
    else:
        rows=(size-1)*2+1
        cols=(size-1)*4+1
        center =int((rows-1)/2+1)
        ec=int((cols-1)/2+1)
        txtfin=''

        for i in range(1,rows+1):
            if i<=center:
                num=i
                txt='-'*cols
                txt=list(txt)
                aux=''
                for j in range(1,num*2):
                    txt[ec-(num-1)*2+(j-1)*2-1]=abc[(size-num+1)+abs(num-j)-1]
                for elem in txt:
                    aux=aux+elem
                txtfin=txtfin+aux+'\n'
            else:
                num=rows-i+1
                txt='-'*cols
                txt=list(txt)
                aux=''
                for j in range(1,num*2):
                    txt[ec-(num-1)*2+(j-1)*2-1]=abc[(size-num+1)+abs(num-j)-1]
                for elem in txt:
                    aux=aux+elem
                txtfin=txtfin+aux+'\n'
    return txtfin
print(solve(size))
