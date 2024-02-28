n = int(input())
a = []
s = []
for i in range(n):
    a.append(input())
c = input()
for i in a:
    if i[-1] == c:
        s.append(i)
print(len(s))
for i in s:
    print(i)