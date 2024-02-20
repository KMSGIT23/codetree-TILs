a, b = map(int, input().split())
b //= (a / 100) ** 2
print(int(b))
if b >= 25:
    print('Obesity')