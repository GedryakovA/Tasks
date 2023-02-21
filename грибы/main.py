n = int(input())
if n % 100 >= 11 and n % 100 <= 14:
    print('грибов')
else:
    if n % 10 == 1:
        print('гриб')
    elif n % 10 >= 2 and n % 10 <= 4:
        print('гриба')
    else:
        print('грибов')

n = int(input())
if n % 100 >= 11 and n % 100 <= 14:
    print('грибов')
elif n % 10 == 1:
        print('гриб')
elif n % 10 >= 2 and n % 10 <= 4:
    print('гриба')
else:
    print('грибов')