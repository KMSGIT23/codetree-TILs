c = input()
a = []
for i in range(200):
    s = input()
    a.append(s)
    if s == '0':
        break
print(len(a))
for i in range(len(a)):
    if i % 2 == 0:
        print(a[i])