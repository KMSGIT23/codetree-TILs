n = int(input())
cnt = 0
for i in range(1, 101):
    if n <= cnt:
        print(i)
        break
    cnt += 1