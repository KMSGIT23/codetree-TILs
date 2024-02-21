n = int(input())
a = list(map(int, input().split()))
f, s = 0, 0
for i in a:
    if i % 5 == 0:
        f += 1
    if i % 7 == 0:
        s += 1
print(f)
print(s)