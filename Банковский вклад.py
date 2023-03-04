startS = int(input())
percent = int(input())
targetS = int(input())
mouthCount = 0
resultS = 0
while startS <= targetS:
    startS = round(startS + percent * startS / 100, 2)
    mouthCount += 1
    print(f" {mouthCount} - {startS}")
resultS = startS
print(f"Кол-во месяцев:{mouthCount}")
print(f"Итоговая сумма:{resultS}")