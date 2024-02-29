a, b = input().split()
a = int(a)
s = []
for i in range(a):
    c = input()
    if b == c[3]:
        s.append(c)
print(len(s))
for i in s:
    print(i)