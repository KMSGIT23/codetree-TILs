a, b = map(int, input().split())
c = []
c.append(1 if a < b else 0)
c.append(1 if a == b else 0)
print(*c)