n = int(input())
pos = 0
zero = 0
neg = 0
for i in range(n):
    x = int(input())
    if x > 0:
        pos += 1
    elif x < 0:
        neg +=1
    else:
        zero +=1
print(f"Положительных: {pos}")
print(f"Отрицательных: {neg}")
print(f"Нулей: {zero}")
