'''
a, b = map(int, input().split())
c = round(a / b, 1)
print(c, end = '')
a = a * 10 % b
for _ in range(19):
    a *= 10
    print(a//b, end='')
    a %= b
'''
a, b= map(int, input().split())

print(f'{a//b}.', end='')

a %= b
for _ in range(20):
    a *= 10
    print(a//b, end='')

    a %= b