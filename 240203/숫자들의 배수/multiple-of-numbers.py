n = int(input())
cnt = 0
for i in range(n, n*10+1, n):
    if cnt == 2:
        break
    print(i, end = ' ')
    if i % 5 == 0:
        cnt += 1