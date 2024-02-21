a = int(input())
for i in range(a):
    n = int(input())
    if n == 0:
        break
    else:
        if n % 3 == 0:
            print(n // 3)
        else:
            print(n + 2)