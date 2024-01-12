a, b = map(int, input().split())
a = (a / 100)**2
b = int(b // a)
print(b)
if b >= 25:
    print('Obesity')