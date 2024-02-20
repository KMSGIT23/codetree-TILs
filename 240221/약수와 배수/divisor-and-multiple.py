n = int(input())
a = list(map(int, input().split()))
k = int(input())
l, r = 0, 0
for i in a:
    if i % k == 0:
        l += i
    if k % i == 0:
        r += i
print(r)
print(l)