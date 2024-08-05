size=3

def solve(size):
    cols=1
    def alfabeto():
        lstret=[]
        for k in range(97,123):
            lstret.append(chr(k))
        return lstret
    abc=alfabeto()
    def fillrowup(num):
        txt='-'*cols
        txt=list(txt)
        aux=''
        for j in range(1,num*2):
            txt[ec-(num-1)*2+(j-1)*2-1]=abc[(size-num+1)+abs(num-j)-1]
        for elem in txt:
            aux=aux+elem
        return aux
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
                txtfin=txtfin+fillrowup(i)+'\n'
            else:
                txtfin=txtfin+fillrowup(rows-i+1)+'\n'
    return txtfin
print(solve(size))


    