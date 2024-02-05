n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
anw = 0
for i in b:
    for j in a:
        if i == j:
            a.remove(j)
            anw = 1
            break
        else:
            a.remove(j)
            anw = 0
print('Yes' if anw == 1 else 'No')