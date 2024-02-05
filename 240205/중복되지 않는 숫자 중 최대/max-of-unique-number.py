n = int(input())
a = list(map(int, input().split()))
b = [0 for i in range(max(a))]
for i in a:
    b[i-1] += 1
m = -1
for i in range(max(a)):
    if b[i] == 1 and m < i + 1:
        m = i + 1
print(m)