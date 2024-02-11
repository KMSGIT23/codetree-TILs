s = input()
while len(s) != 2:
    s = list(s)
    n = int(input())
    s.remove(s[n])
    s = ''.join(s)
    print(s)
print(s[0])