n = int(input())
p, q = 0, 0
a = []
for i in range(n):
    c = input()
    a.append(c)
w = input()
for i in a:
    if i[0] == w:
        p += 1
        q += len(i)
print("%d %.2f"%(p, q/p))