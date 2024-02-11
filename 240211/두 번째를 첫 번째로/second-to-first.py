w = list(input())
f = w[0]
s = w[1]
for i in range(len(w)):
    if w[i] == s:
        w[i] = f
w = ''.join(w)
print(w)