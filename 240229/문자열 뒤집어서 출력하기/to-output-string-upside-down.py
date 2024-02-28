a = []
for i in range(4):
    s = input()
    a.append(s[::-1])
for i in range(3, -1, -1):
    print(a[i])