a, b = map(int, input().split())
anw = 0
for i in range(a, b+1):
    if 1920 % i == 0:
        if 2880 % i == 0:
            anw = 1
print(anw)