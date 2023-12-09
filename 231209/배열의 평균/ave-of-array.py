a = []
for i in range(2):
    p = list(map(int, input().split()))
    a.append(p)
print("%.1f %.1f "%(sum(a[0]) / 4, sum(a[1]) / 4))
for i in range(4):
    print("%.1f "%((a[0][i] + a[1][i]) / 2), end = '')

print("%.1f"%((sum(a[0]) + sum(a[1])) / 8))