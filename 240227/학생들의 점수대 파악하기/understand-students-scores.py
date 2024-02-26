n = int(input())
a = list(map(int, input().split()))
s = [0 for i in range(10)]
for i in a:
    if i >= 10:
        s[i // 10 - 1] += 1
for i in range(9, -1, -1):
    if s[i] != 0:
        print((i + 1) * 10, '-', s[i])