a = []
m = 0
j = 0
for i in range(5):
    a.append(input())
    m = max(m, len(a[-1]))
i = 0
for k in range(5 * m):
    if len(a[i]) > j:
        print(a[i][j], end = '')
    i += 1
    if i == 5:
        i = 0
        j += 1