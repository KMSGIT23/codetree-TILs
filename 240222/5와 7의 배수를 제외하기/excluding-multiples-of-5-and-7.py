n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] % 5 == 0 or a[i] % 7 == 0:
        del a[i]
print(sum(a))
print("%.1f"%(sum(a) / len(a)))