arr = list(map(int, input().split()))
s = []
t = []
for i in range(1, 11):
    if i % 2 == 0:
        s.append(i)
    if i % 3 == 0:
        t.append(i)
print("%d %.1f"%(sum(s), sum(t) / len(t)))