if __name__ == '__main__':
    N = int(input())
    list=[]
    lstCmd = ['insert','print','remove','append','sort','pop','reverse']
    for i in range(N):
        while True:
            cmdLine = str(input())
            cmdParts= cmdLine.split()
            cmdWord = cmdParts[0]
            if len(cmdParts)>1:
                param1=int(cmdParts[1])
            if len(cmdParts)>2:
                param2=int(cmdParts[2])
            if cmdWord in lstCmd:
                match cmdWord:
                    case 'insert':
                        list.insert(param1,param2)
                    case 'print':
                        print(list)
                    case 'remove':
                        list.remove(param1)
                    case 'append':
                        list.append(param1)
                    case 'sort':
                        list.sort()
                    case 'pop':
                        list.pop()
                    case 'reverse':
                        list.reverse()
                break
            else:
                print(f'El comando "{cmdWord}" no es valido. Por favor, ingrese uno de la siguiente lista: "{lstCmd}".')
