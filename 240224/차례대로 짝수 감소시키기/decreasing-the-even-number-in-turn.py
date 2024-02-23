n = int(input())
cnt = 2
c = 0
i = 1000

while i > n:
    if i % 2 == 0:
        c += 1
    i -= cnt
    cnt += 2

print(c, (c * (c + 1)) // 2 * 2)