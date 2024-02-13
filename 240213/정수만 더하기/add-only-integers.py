x = input()
s = []
for i in range(len(x)):
    if 49 <= ord(x[i]) <= 57:
        s.append(int(x[i]))
print(sum(s))