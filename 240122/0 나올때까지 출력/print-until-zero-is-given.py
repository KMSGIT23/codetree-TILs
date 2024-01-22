last = []

while True:
    try:
        n = int(input())
        if n != 0:
            last.append(n)
        else:
            for i in last:
                print(i)
    except:
        break