n, m = map(int, input().split())
cnt = 0
a = list(map(int, input().split()))

for i in a:
    if i == m:
        cnt += 1

print(cnt)