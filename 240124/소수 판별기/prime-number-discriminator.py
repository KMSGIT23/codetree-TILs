n = int(input())
anw = 'P'
for i in range(2, n):
    if n % i == 0:
        anw = 'C'
print(anw)