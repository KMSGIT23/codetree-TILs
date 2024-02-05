n = int(input())
a = list(map(int, input().split()))
m = -1
for i in a:
    if m <= i:
        if m != i:
            m = i
        else:
            m = -1
print(m)