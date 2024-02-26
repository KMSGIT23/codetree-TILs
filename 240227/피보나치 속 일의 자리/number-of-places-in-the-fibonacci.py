n = int(input())
a, b = map(int, input().split())
s = [a, b]
for i in range(1, n-1):
    s.append((s[i] + s[i-1]) % 10)
print(*s)