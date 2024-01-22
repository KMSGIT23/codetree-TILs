last = []
while True:
    n = int(input())
    if n != 0:
        last.append(n)
    else:
        for i in last:
            print(i)