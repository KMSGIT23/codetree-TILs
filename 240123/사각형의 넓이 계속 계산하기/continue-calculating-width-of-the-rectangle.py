while True:
    try:
        a, b, c =input().split()
        print(int(a) * int(b))
        if c == 'C':
            break
    except:
        break