n, m = map(int, input().split())
lst_vals = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

hapiness = 0
for elem in lst_vals:
    if elem in set_a:
        hapiness += 1
    elif elem in set_b:
        hapiness -= 1

print(hapiness)
