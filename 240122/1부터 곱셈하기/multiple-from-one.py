n = int(input())
cnt = 1
for i in range(1, 10):
    cnt *= i
    if cnt >= n:
        print(i)
        break