n = int(input())
cnt = 1
r = n
for i in range(n):
    if i % 2 == 0:
        for j in range(cnt, n+1):
            print(j, end = ' ')
            cnt += 1
        n += r*2
        cnt += 1
        print()
    else:
        for j in range(cnt, n+1, 2):
            print(j, end = ' ')
            cnt += 2
        n += r
        cnt -= 1
        print()