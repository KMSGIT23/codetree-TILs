a = []
while True:
    try:
        n = int(input())
        if 29 >= n and n >= 20:
            a.append(n)
        else:
            print("%.2f"%(sum(a) / len(a)))
            break
    except:
        break