a, b = map(int, input().split())
c = str(a / b)
print(c[:3], end = '')
a = a % b * 10 % b
for _ in range(19):
    a *= 10
    print(a//b, end='')
    a %= b