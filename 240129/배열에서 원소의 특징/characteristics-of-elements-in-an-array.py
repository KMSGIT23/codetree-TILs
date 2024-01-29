a = list(map(int, input().split()))
r = 0
for i in a:
    if i % 3 == 0:
        break
    r = i
print(r)