a = list(input().split())
s = []
for i in range(len(a)):
    if i % 2 != 0:
        s.append(a[i])
for i in s:
    print(i)