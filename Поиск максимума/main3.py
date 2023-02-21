n = int(input())
max_num = -10000
min_num = 10000
poz_max = 1
poz_min = 1
i = 0
s = 0
while i < n:
    x = int(input())
    s += 1
    if x > max_num:
        max_num = x
        poz_max = s
    elif x < min_num:
        min_num = x
        poz_min = s
    i += 1
print(f'Минимальное число: {min_num}, позиция {poz_min}')
print(f'Максимальное число: {max_num}, позиция {poz_max}')
