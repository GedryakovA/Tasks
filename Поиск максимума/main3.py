n = int(input())
max_num = -10000
min_num = 10000
poz_max = 0
poz_min = 0
i = 0
while i < n:
    x = int(input())
    if x > max_num:
        max_num = x
        poz_max = i+1
    elif x < min_num:
        min_num = x
        poz_min = i+1
    i += 1
print(f'Минимальное число: {min_num}, позиция {poz_min}')
print(f'Максимальное число: {max_num}, позиция {poz_max}')
