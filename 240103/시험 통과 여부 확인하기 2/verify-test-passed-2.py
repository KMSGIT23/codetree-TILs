n = int(input())
s = 0
for i in range(n):
    a = list(map(int, input().split()))
    if sum(a) / 4 >= 60:
        print('pass')
        s += 1
    else:
        print('fail')
print(s)