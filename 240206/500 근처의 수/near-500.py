a = list(map(int, input().split()))
b = []
for i in a:
    if i > 500:
        b.append(i)
        a.remove(i)
print(max(a), min(b))