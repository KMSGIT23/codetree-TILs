n = int(input())
a = int(input())
if n == 0:
    print('M' if a >= 19 else 'B')
else:
    print('W' if a >= 19 else 'G')