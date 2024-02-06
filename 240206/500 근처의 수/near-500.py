a = list(map(int, input().split()))
b = []
c = []
for i in a:
    if i > 500:
        b.append(i)
    else:
        c.append(i)
print(max(c), min(b))