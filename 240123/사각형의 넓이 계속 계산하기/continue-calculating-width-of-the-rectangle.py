while True:
    try:
        a, b, c =input().split()
        print(a * b)
        if c == 'C':
            break
    except:
        break