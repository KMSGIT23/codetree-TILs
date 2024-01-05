a = list(map(int, input().split()))
h = 0
jj = 0
for i in range(len(a)):
    if i % 2 == 0:
        jj += a[i]
    else:
        h += a[i]
if jj > h:
    print(jj - h)
else:
    print(h - jj)