a = [0 for i in range(4)]
for i in range(3):
    n, m = input().split()
    if n == 'Y' and int(m) >= 37:
        a[0] += 1
    elif n == 'Y' and int(m) < 37:
        a[2] += 1
    elif n == 'N' and int(m) >= 37:
        a[1] += 1
    else:
        a[3] += 1
if a[0] >= 2:
    print(*a, 'E')
else:
    print(*a)