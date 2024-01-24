n = int(input())
s = 'N'
for i in range(2, n+1):
    if n % i == 0:
        s = 'C'
        break
print(s)