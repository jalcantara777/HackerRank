n=int(input())
lst_vals=list(input().rstrip().split())
print(all([eval(expr) for expr in list(x+">0" for x in lst_vals)]) and any([eval(expr) for expr in list(x+"in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,11, 22, 33, 44, 55, 66, 77, 88, 99]" for x in lst_vals)]))