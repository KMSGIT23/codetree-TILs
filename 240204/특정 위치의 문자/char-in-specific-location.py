a = ['L', 'E', 'B', 'R', 'O', 'S']
n = input()
if n in a:
    for i in range(6):
        if n == a[i]:
            print(i)
            break
else:
    print('None')