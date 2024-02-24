n = int(input())
cnt = 2
for i in range(n):
    print('  ' * i, end = '')
    for j in range(n - i):
        print(cnt, end = ' ')
        cnt += 2
        if cnt > 8:
            cnt = 2
    print()