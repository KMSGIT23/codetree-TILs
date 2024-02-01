a = list(map(int, input().split()))
print(*a, end = ' ')
for i in range(1, 9):
    print((a[i-1]+a[i]) % 10, end = ' ')
    a.append((a[i-1]+a[i]) % 10)