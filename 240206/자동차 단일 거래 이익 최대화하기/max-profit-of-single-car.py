n = int(input())
a = list(map(int, input().split()))
a = a[a.index(min(a)):]
if len(a) == 1:
    print(0)
else:
    print(max(a) - min(a))