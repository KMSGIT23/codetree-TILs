n = int(input())
cnt = 0
for i in range(1, 101):
    if n <= cnt:
        print(cnt)
        break
    cnt += i