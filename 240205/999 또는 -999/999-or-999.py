a = list(map(int, input().split()))
b = []
for i in a:
    if i == 999 or i == -999:
        break
    b.append(i)
print(max(b), min(b))