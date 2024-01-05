a = list(map(int, input().split()))
h = 0
jj = 0
for i in a:
    if i % 2 == 0:
        jj += i
    else:
        h += i
if jj > h:
    print(jj - h)
else:
    print(h - jj)