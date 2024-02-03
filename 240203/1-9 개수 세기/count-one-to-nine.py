n = int(input())
a = list(map(int, input().split()))
b = [0 for _ in range(9)]
for i in a:
    b[i-1] += 1
for i in b:
    print(i)