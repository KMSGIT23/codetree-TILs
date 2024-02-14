n, a = input().split(); n = int(n)
cnt = 0
for i in range(n):
    b = input()
    if b == a:
        cnt += 1
print(cnt)