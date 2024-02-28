n = int(input())
for i in range(n):
    c = input()
    if ord(c) < 65:
        print(ord(c))
    else:
        print(c)