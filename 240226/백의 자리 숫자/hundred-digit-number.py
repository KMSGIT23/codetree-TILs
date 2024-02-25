n = int(input())
a = list(map(int, input().split()))
s = [0 for i in range(10)]
for i in a:
    s[i // 100] += 1
for i in range(len(s)):
    if s[i] != 0:
        print(i, '-', s[i])