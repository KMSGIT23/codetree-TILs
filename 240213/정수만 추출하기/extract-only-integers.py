s1, s2 = input().split()
a = []; b = []
for i in range(len(s1)):
    if 48 <= ord(s1[i]) <= 57:
        a.append(s1[i])
    else:
        break
a = int(''.join(a))
for i in range(len(s2)):
    if 48 <= ord(s2[i]) <= 57:
        b.append(s2[i])
    else:
        break
b = int(''.join(b))
print(a+b)