n = int(input())
cnt = 0
for i in range(n, 0, -1):
    print(' ' * cnt, end = '')
    for j in range(i, 0, -1):
        print(j, end = ' ')
    cnt += 2
    print()