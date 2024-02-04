a, b = map(int, input().split())
arr = [0 for i in range(10)]
while a > 1:
    arr[a%b] += 1
    a //= b
for i in range(10):
    arr[i] = arr[i] ** 2
print(sum(arr))