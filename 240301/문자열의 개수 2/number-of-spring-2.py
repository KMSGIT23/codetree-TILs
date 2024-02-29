c = input()
a = []
for i in range(200):
    s = input()
    if s == '0':
        break
    a.append(s)
print(len(a))
for i in range(len(a)):
    if i % 2 == 0:
        print(a[i])