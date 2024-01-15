a, b = input().split()
c, d = input().split()
print(1 if (int(a) > 18 or int(c) > 18) and (b == 'M' or d == 'M') else 0)