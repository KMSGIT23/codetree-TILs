n = int(input()); sum = 0
for i in range(n):
    a = int(input())
    sum += a
print(n, round(sum / n, 1))