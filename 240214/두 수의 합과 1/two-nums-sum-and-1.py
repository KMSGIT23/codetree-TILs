a, b = map(int, input().split())
a = str(a+b)
cnt = 0
for i in range(len(a)):
    if a[i] == '1':
        cnt += 1
print(cnt)