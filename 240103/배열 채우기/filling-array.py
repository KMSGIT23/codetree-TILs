a = list(map(int, input().split()))
b = []
for i in a:
    if i == 0:
        break
    b.append(i)
print(*b[::-1])