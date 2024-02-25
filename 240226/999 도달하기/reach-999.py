n = int(input())
a = [1, n]
cnt = sum(a)
i = 2
while cnt < 1000:
    a.append(cnt)
    cnt = a[i] + a[i-1]
    i += 1
a.append(cnt)
print(*a)