cnt = 0
while True:
    try:
        if cnt == 3:
            break
        n = int(input())
        if n % 2 == 0:
            print(n // 2)
            cnt += 1
    except:
        break