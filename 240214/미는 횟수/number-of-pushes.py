a = input()
b = input()
cnt = 0
for i in range(len(a)):
    if a == b:
        break
    a = a[-1] + a[:-1]
    cnt += 1
print(cnt if cnt != len(a) else -1)