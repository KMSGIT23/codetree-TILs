a, b = map(int, input().split())
for i in range(a, b + 1):
    if a > b:
        break
    print(a, end = ' ')
    if a % 2 == 0:
        a += 3
    else:
        a *= 2