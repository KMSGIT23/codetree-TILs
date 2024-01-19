a = []
cnt = 0
for i in range(10):
    n = int(input())
    a.append(n)
for i in a:
    if i % 2 == 1:
        cnt += 1
print(cnt)