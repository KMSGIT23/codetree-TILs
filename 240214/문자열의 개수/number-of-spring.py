a = []
cnt = 0
i = 0
while True:
    n = input()
    if n == '0':
        break
    if i % 2 == 0:
        a.append(n)
    cnt += 1
    i += 1
print(cnt)
for i in a:
    print(i)