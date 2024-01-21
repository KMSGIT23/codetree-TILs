cnt = 0; sum = 0
for i in range(10):
    n = int(input())
    if n >= 0 and n <= 200:
        cnt += 1
        sum += n

print(sum, round(sum/cnt, 1))