n = int(input())
a = list(map(int, input().split()))
b = []
for i in range(n):
    if i % 2 == 1:
        b.append(a[i])
print("%d %.1f"%(sum(b), sum(b) / len(b)))