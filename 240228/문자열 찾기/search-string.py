s = input()
k = 0
io = 0
for i in range(len(s)):
    if s[i:i + 3] == 'KOI':
        k += 1
    if s[i:i + 3] == 'IOI':
        io += 1
print(k, io)