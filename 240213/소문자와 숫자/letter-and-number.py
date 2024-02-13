x = input()
s = []
for i in range(len(x)):
    if 90 >= ord(x[i]) >= 65 or 97 <= ord(x[i]) <= 122:
        s.append(x[i].lower())
    elif 48 <= ord(x[i]) <= 57:
        s.append(x[i])
    else:
        continue
print(''.join(s))