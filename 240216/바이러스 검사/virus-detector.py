n = int(input())
a = list(map(int, input().split()))
p, q = map(int, input().split())
cnt = 0
for i in a:
    i -= p
    if i > q:
        if i % q == 0:
            cnt += i // q + 1
        else:
            cnt += i // q + 2
    else:
        if i <= 0:
            cnt += 1
        else:
            cnt += 2
print(cnt)