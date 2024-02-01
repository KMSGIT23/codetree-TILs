n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    q = 1
    for j in range(a, b+1):
        q *= j
    print(q)