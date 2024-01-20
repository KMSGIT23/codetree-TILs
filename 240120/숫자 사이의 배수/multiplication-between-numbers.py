a, b = map(int, input().split())
c = []
for i in range(a, b+1):
    if i % 5 == 0 or i % 7 == 0:
        c.append(i)
print("%d %.1f"%(sum(c), sum(c) / len(c)))