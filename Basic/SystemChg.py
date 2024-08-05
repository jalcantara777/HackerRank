number=int(17)

def quotas(num,base):
    lstq=[]
    quot=num
    while quot>=base:
        rest=quot%base
        if base==16 and rest>9:
            rest=chr(55+rest)
        quot=quot//base
        lstq.append(rest)
    quot=chr(55+quot) if (base==16 and quot>9) else quot
    lstq.append(quot)
    return lstq

def cadlistrev(lst):
    txtret=''
    for i in range(len(lst),0,-1):
        txtret=txtret+str(lst[i-1])
    return txtret

widht=len(cadlistrev(quotas(number,2)))

for j in range(1,number+1):
    print(repr(j).rjust(widht),cadlistrev(quotas(j,8)).rjust(widht),cadlistrev(quotas(j,16)).rjust(widht),cadlistrev(quotas(j,2)).rjust(widht))   

    