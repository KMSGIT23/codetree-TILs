n = list(input())
f = n[0]
s = n[1]
for i in range(len(n)):
    if n[i] == f:
        n[i] = s
    elif n[i] == s:
        n[i] = f
n = ''.join(n)
print(n)