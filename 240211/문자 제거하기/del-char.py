s = input()
while len(s) != 1:
    s = list(s)
    n = int(input())
    if n >= len(s):
        s.pop()
    else:
        del s[n]
    s = ''.join(s)
    print(s)