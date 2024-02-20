n = int(input())
for i in range(n):
    a = int(input())
    if a > 0:
        print('plus')
    elif a < 0:
        print('minus')
    else:
        print('zero')