n = int(input())
a = []
for i in range(n):
    p = int(input())
    a.append(p)
for i in a:
    if i % 3 == 0 and i % 2 == 1:
        print(i)