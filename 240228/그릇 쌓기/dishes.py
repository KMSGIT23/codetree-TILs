s = list(input())
h = 10
f = s[0]
for i in range(1, len(s)):
    if s[i] == f:
        h += 5
    else:
        h += 10
        f = s[i]
print(h)