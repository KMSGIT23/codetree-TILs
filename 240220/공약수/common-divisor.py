n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
if n == 2:
    for i in range(1, arr[0] + 1):
        if arr[0] % i == 0 and arr[1] % i == 0:
            print(i)
else:
    for i in range(1, arr[0] + 1):
        if arr[0] % i == 0 and arr[1] % i == 0 and arr[2] % i == 0:
            print(i)