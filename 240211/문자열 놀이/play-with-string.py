s, q = input().split(); q = int(q)
for i in range(q):
    a, b, c = input().split()
    s = list(s)
    a = int(a)
    if a == 1:
        b, c = int(b) - 1, int(c) - 1
        temp = s[b]
        s[b] = s[c]
        s[c] = temp
    else:
        for j in range(len(s)):
            if s[j] == b:
                s[j] = c
    s = ''.join(s)
    print(s)