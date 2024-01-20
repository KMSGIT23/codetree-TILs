arr = list(map(int, input().split()))
a, b = min(arr), max(arr)
sum = 0
for i in range(a, b+1):
    if i % 5 == 0:
        sum += i
print(sum)