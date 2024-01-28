n = int(input())
j = n - 1
for i in range(1, n):
    print('  ' * j, end = '')
    print('@ ' * i)
    j -= 1

for i in range(n, 0, -1):
    print('@ ' * i)