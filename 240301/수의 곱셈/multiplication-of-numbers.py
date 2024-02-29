n = list(map(int, input().split()))
n.sort()
m = n[0] * n[-1]
for i in range(1, 3):
    if n[i-1] * n[i] > m:
        if n[i-1] * n[i] % 2 == 0 and m % 2 != 0:
            continue
        else:
            m = n[i-1] * n[i]
print(m)