a = []
for i in range(3):
    a.append(list(map(int, input().split())))
for i in range(3):
    print("%.1f"%(sum(a[i])/ 3), end = ' ')
print()
for i in range(3):
    cnt = 0
    for j in range(3):
        cnt += a[j][i]
    print("%.1f"%(cnt / 3), end = ' ')
print()
print("%.1f"%(sum(a[0] + a[1] + a[2]) / 9))