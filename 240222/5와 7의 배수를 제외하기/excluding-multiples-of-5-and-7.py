n = int(input())
arr = list(map(int, input().split()))
a = []
for i in arr:
    if i % 5 != 0 or i % 7 != 0:
        a.append(i)
print(sum(a))
print("%.1f"%(sum(a) / len(a)))