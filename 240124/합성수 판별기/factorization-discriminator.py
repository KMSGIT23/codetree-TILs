n = int(input())
s = 'N'
for i in range(2, n):
    if n % i == 0:
        s = 'C'
        break
print(s)