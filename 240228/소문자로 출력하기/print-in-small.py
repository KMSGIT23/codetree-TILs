s = list(input())
a = []
for i in range(len(s)):
    if 65 <= ord(s[i]) <= 90 or 97 <= ord(s[i]) <= 122:
        a.append(s[i].lower())
for i in a:
    print(i, end = '')