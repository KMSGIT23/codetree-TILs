a = list(map(int, input().split()))
b = []
for i in a:
    if i < 249:
        b.append(i)
    else:
        break
print("%d %.1f"%(sum(b), sum(b) / len(b)))