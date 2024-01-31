n = int(input())
t = 65
for i in range(n):
    for j in range(n):
        print(chr(t), end = '')
        t += 1
    print()