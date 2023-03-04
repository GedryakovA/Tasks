n = int(input())
i = 1
c = int(input())
p = 0
max_p = 0
while i < n:
    x = int(input())
    i += 1
    if c < x:
        p += 1
    else:
        if p > max_p:
            max_p = p
        p = 0
    c = x
if p > max_p:
    max_p = p
print(max_p + 1)
print(p+1 if p > max_p else max_p+1)


