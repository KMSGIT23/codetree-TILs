n = int(input())
a = list(input().split())
b = []
s = ''
r = 0
for i in a:
    s += i
for i in range(len(s)):
    if i % 5 == 0 and i != 0:
        print(s[r:i])
        r = i
        b.append(s[r:i])
print(len(b))