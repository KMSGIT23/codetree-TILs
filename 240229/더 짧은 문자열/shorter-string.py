a, b = input().split()
if len(a) == len(b):
    print('equal')
else:
    print(a, len(a) if len(a) < len(b) else b, len(b))