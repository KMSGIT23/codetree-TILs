arr = list(input().split())
a, b = max(arr), min(arr)
print(ord(a) + ord(b), ord(a) - ord(b))