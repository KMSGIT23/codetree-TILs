a = list(map(int, input().split()))
print(1 if a[0] == min(a) else 0, end = ' ')
print(1 if a[0] == a[1] == a[2] else 0)