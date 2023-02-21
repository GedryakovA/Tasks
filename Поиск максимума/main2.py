n = int(input())
min_num = 10000
i = 0
while i < n:
    x = int(input())
    if x < min_num:
        min_num = x
    i += 1
print(min_num)