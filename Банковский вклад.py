startS = int(input())
percent = int(input())
targetS = int(input())
mouthCount = 0
while startS <= targetS:
    startS = startS + percent * startS / 100
    mouthCount += 1
    print(f"{mouthCount} - {startS:.2f}")
print(f"Кол-во месяцев: {mouthCount}")
print(f"Итоговая сумма: {startS:.2f}")
