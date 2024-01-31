n = int(input())
t = 65
for i in range(n):
    for j in range(i+1):
        print(chr(t), end = '')
        if t == 90:
            t = 65
        else:
            t += 1
    print()