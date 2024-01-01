a = list(map(int, input().split()))
if a[-1] == 0:
    a.pop()
    a.reverse()
    print(*a)
else:
    a.reverse()
    print(*a)