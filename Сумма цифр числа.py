n = int(input())
x = 0
sum = 0
while n > 0:
    sum += n % 10
    n = n // 10
    x += 1
print(x)
print(sum)

