n = int(input())
t = 65
for i in range(1, n+1):
    for j in range(i):
        print(chr(t), end = '')
        t += 1
    print()