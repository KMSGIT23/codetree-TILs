n = int(input())
a = []
for i in range(n, 501):
    if i % 2 == 0:
        a.append(i)
print(sum(a))