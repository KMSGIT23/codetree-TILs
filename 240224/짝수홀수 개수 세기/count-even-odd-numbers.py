n = int(input())
a, b = 0, 0
for i in range(n):
    p = int(input())
    if p == 0:
        break
    if p % 2 == 0:
        a += 1
    else:
        b += 1
print(a)
print(b)