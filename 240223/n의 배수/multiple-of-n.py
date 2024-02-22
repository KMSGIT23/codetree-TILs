n = int(input())
for i in range(n, 200, n):
    print(i, end = '')
    if i % 10 == 0:
        break