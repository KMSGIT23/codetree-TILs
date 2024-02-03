a = list(map(int, input().split()))
a.pop()
for i in a:
    if i % 2 == 1:
        print(i + 3, end = ' ')
    else:
        print(i // 2, end = ' ')