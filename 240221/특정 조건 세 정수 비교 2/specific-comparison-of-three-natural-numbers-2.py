a, b, c = map(int, input().split())
print(1 if b > a and b > c else 0, 1 if a == b == c else 0)