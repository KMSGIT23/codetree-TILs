n = int(input())
a = [1]
i = 1
a.append(n)
while True:
    a.append(a[i-1]+a[i])
    if a[i-1]+a[i] > 100:
        break
    i += 1
print(*a)