from itertools import permutations
cad,k=input().split()
k=int(k)
lstperm= list(permutations(cad,k))
lst2ret=[]
for i in range(len(lstperm)):
    cadaux=''.join(str(x) for x in lstperm[i])
    lst2ret.append(cadaux)
lst2ret.sort()
for i in range(len(lst2ret)):
    print(lst2ret[i])