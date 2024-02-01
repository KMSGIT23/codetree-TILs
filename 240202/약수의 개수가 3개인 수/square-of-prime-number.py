s, e = map(int, input().split())
b = 0
for i in range(s, e+1):
    a = []
    for j in range(1, i+1):
        if i % j == 0:
            a.append(j)
    if len(a) == 3:
        b += 1
print(b)