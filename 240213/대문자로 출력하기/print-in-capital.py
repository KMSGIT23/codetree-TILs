x = input()
s = []
for i in range(len(x)):
    if ord(x[i]) >= 65 and ord(x[i]) <= 122:
        s.append(x[i].upper())
print(''.join(s))