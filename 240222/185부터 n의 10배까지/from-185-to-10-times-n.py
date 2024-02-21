n = int(input())
a = []
for i in range(185, n*10+1):
    a.append(i)
print("%d %.1f"%(sum(a), sum(a) / len(a)))