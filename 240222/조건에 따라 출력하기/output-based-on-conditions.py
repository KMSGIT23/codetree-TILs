while True:
    n = int(input())
    if n == 0:
        break
    if n % 3 == 0:
        print(n // 3)
    else:
        print(n + 3)