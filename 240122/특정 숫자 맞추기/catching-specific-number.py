while True:
    try:
        n = int(input())
        if n == 25:
            print('Good')
            break
        else:
            print('Higher' if n > 25 else 'Lower')
    except:
        break