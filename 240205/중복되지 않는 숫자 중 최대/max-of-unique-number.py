n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    if a == []:
        break
    m = max(a)
    a.remove(max(a))
    if m in a:
        a.remove(max(a))
        m = -1
    else:
        break
print(m)