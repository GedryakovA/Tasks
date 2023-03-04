c = int(input())
inc = dec = 1
max_l = 0
while c != 0:
    max_l = max(max_l, dec, inc)
    x = int(input())
    if c > x:
        inc += 1
        dec = 1
    elif c < x:
        dec += 1
        inc = 1
    else:
        inc = dec = 1
    c = x
print(max_l)
