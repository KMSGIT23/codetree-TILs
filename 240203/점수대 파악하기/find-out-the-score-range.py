a = list(map(int, input().split()))
b = [0 for _ in range(10)]
for i in a:
    if i == 0:
        break
    if i // 10 != 0:
        b[i//10-1] += 1
j = 9
b = b[::-1]
for i in range(10):
    print((j+1)*10, '-', b[i])
    j -= 1