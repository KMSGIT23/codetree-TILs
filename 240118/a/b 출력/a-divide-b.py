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
arr=input().split()
a, b= int(arr[0]), int(arr[1])

print(f'{a//b}.', end='')

a %= b
for _ in range(20):
    a *= 10
    print(a//b, end='')

    a %= b