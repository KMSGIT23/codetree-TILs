a = list(map(int, input().split()))
s = []
t = []
for i in range(1, 11):
    if i % 2 == 0:
        s.append(a[i-1])
    if i % 3 == 0:
        t.append(a[i-1])
print("%d %.1f"%(sum(s), sum(t) / len(t)))