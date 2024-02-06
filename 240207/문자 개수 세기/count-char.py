a = input()
n = input()
cnt = 0
for i in range(len(a)):
    if a[i] == n:
        cnt += 1
print(cnt)