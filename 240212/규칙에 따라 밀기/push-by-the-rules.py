n = input()
a = list(input())
for i in a:
    if i == 'L':
        n = n[1:] + n[0]
    else:
        n = n[-1] + n[:-1]
print(n)