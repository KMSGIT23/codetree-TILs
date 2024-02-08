n = int(input())
a = []
cnt = 0
c = 0
for i in range(n):
    word = input()
    a.append(word)
for i in a:
    cnt += len(i)
    if i[0] == 'a':
        c += 1
print(cnt, c)