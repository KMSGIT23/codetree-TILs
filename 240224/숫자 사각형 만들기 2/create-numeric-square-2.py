a, b = map(int, input().split())
cnt = a * b
for i in range(a):
    for j in range(b):
        print(cnt, end = ' ')
        cnt -= 1
    print()