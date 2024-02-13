x = input()
s = []
for i in range(len(x)):
    if 90 >= ord(x[i]) >= 65 or 97 <= ord(x[i]) <= 122:
        s.append(x[i].upper())
print(''.join(s))