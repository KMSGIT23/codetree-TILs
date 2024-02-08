a = []
cnt = 0
for i in range(10):
    w = input()
    a.append(w)
n = input()
for i in a:
    if i[-1] == n:
        print(i)
        cnt += 1
if cnt == 0:
    print('None')