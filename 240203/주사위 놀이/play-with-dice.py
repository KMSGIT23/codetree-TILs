a = list(map(int, input().split()))
b = [0 for _ in range(6)]
for i in a:
    b[i-1] += 1
for i in range(6):
    print(i+1, "-", b[i])