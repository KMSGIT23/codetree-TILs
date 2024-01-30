n = int(input())
for i in range(1, n*n, n):
    for j in range(i, i+n):
        print(j, end = ' ')
    print()