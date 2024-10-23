from collections import Counter

# number of shoes
x=int(input())

# list of shoe sizes
shoesize_lst=list(int(x) for x in input().split())

# number of customers
n=int(input())

# to get of sold shoe size and sell price
lst_sell_shoesz=[]
lst_sell_price =[]
for i in range(n):
  shoesz,price=input().split()
  lst_sell_shoesz.append(int(shoesz))
  lst_sell_price.append(int(price))

# selling calculate
tot_sell=0
for i in range(len(Counter(lst_sell_shoesz).keys())):
  shoesz_req=list(Counter(lst_sell_shoesz).keys())[i]
  if list(Counter(shoesize_lst).keys()).count(shoesz_req)>0:
    shoesz_stk=list(Counter(shoesize_lst).values())[list(Counter(shoesize_lst).keys()).index(shoesz_req)]
    for j in range(shoesz_stk):
      shoepx=lst_sell_price[lst_sell_shoesz.index(shoesz_req,j)]
      tot_sell+=shoepx
print(tot_sell)