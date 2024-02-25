n = int(input())
a = list(map(int, input().split()))
s = [0 for i in range(8)]
for i in a:
    s[i-1] += 1
for i in range(len(s)):
    print(i + 1, '-', s[i])