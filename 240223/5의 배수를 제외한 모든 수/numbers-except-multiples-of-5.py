arr = list(map(int, input().split()))
x, y = min(arr), max(arr)
arr = []
for i in range(x, y+1):
    if i % 5 != 0:
        arr.append(i)
print("%d %.1f"%(sum(ar), sum(arr) / len(arr)))