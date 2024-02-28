s = list(map(ord, input().split()))
a, b = min(s), max(s)
print(a * b, b // a)