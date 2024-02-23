n = int(input())
for i in range(n):
    a, b, c = input().split()
    a, b = int(a), int(b)
    if c == 's':
        print(a * b)
    elif c == 't':
        print("%.1f"%(a * b / 2))