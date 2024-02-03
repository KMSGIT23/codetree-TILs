a = []
while True:
    n = int(input())
    if n == 0:
        break
    a.append(n)

for i in a:
    if i % 2 == 1:
        print(i + 3, end = ' ')
    else:
        print(i // 2, end = ' ')