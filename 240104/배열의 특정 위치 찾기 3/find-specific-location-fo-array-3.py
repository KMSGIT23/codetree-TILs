a = list(map(int, input().split()))
s = []
for i in a:
    if i == 0:
        break
    s.append(i)
s = s[::-1]
print(s[0] + s[1] + s[2])