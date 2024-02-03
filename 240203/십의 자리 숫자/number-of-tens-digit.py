a = list(map(int, input().split()))
b = [0 for _ in range(9)]
for i in a:
    if i == 0:
        break
    if i // 10 != 0:
        b[i//10-1] += 1
for i in range(9):
    print(i+1, '-', b[i])