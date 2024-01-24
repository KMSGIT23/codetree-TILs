a, b, c = map(int, input().split())
anw = 'YES'
for i in range(a, b+1):
    if i % c == 0:
        anw = 'NO'
        break
print(anw)