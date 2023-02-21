n = int(input())
max_num = min_num = int(input())
i = 1
while i < n:
    x = int(input())
    if x > max_num:
        max_num = x
    i += 1
print(max_num)
