a = list(map(int, input().split()))
n = []
for i in a:
    if i == -999:
        break
    n.append(i)
print(max(n), min(n))