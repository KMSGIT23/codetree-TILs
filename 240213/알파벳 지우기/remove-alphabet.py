s = input()
a = []; b = []
for i in range(len(s)):
    if 48 <= ord(s[i]) <= 57:
        a.append(s[i])
a = int(''.join(a))
s = input()
for i in range(len(s)):
    if 48 <= ord(s[i]) <= 57:
        b.append(s[i])
b = int(''.join(b))
print(a+b)