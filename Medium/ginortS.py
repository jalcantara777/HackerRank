cadena=input()
n=len(cadena)
lst_ordkey = []
for i in range(n):
    ordkey=0
    if ord(cadena[i])>=ord('a') and ord(cadena[i])<=ord('z'): ordkey=0
    if ord(cadena[i])>=ord('A') and ord(cadena[i])<=ord('Z'): ordkey=200
    if ord(cadena[i])>=ord('0') and ord(cadena[i])<=ord('9'):
      if int(cadena[i])%2==0:
        ordkey=400
      else:
        ordkey=300
    lst_ordkey.append([cadena[i],ordkey+ord(cadena[i])])
k=1
lst_ord=[]
for i in range(n):
    lst_ord.append(lst_ordkey[i][k])
lst_ord.sort()
lst_ord2d=[]
for i in range(n):
    val2ord=lst_ord[i]
    for j in range(len(lst_ordkey)):
        if lst_ordkey[j][k]==val2ord:
            break
    lst_ord2d.append(lst_ordkey.pop(j))
print("".join(lst_ord2d[i][0] for i in range(len(lst_ord2d))))