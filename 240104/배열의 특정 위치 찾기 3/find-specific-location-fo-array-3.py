a = list(map(int, input().split()))
b = [0]
for i in a:
    if i == 0:
        break
    b.append(i)
print(sum(b))