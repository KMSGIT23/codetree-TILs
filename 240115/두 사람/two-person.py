a, b = input().split()
c, d = input().split()
print(1 if (int(a) >= 19 or int(c) >= 19) and (b == "M" or d == "M") else 0)