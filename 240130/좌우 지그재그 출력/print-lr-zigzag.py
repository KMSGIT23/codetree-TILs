n = int(input())
cnt = 1
r = n
for i in range(n):
    if i % 2 == 0:
        for j in range(cnt, n+1):
            print(j, end = ' ')
            cnt += 1
        n += r
        print()
    else:
        for j in range(n, cnt-1, -1):
            print(j, end = ' ')
        cnt += 1*r
        n += r
        print()