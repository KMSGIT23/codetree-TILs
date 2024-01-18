a, b = map(int, input().split())
c = round(a / b, 1)
print(c, end = '')
a = int(str(c)[-1])
a = a * b % 10
for _ in range(19):
    a *= 10
    print(a//b, end='')

    a %= b