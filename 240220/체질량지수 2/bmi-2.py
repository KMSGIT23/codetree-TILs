a, b = map(int, input().split())
b //= (a // 100) ** 2
print(b)
if a >= 25:
    print('Obesity')