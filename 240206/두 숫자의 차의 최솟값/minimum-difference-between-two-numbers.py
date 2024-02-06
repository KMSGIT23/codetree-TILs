n = int(input())
a = list(map(int, input().split()))
m = 10000
for i in range(n):
    for j in range(n):
        if i < j:
            if a[j] - a[i] < m:
                m = a[j] - a[i]
print(m)