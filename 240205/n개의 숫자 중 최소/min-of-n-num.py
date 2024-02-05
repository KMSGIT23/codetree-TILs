n = int(input())
a = list(map(int, input().split()))
c = 0
for i in a:
    if i == min(a):
        c += 1
print(min(a), c)