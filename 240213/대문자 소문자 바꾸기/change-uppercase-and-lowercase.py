s = input()
for i in range(len(s)):
    if 97 <= ord(s[i]) <= 122:
        print(s[i].upper(), end = '')
    else:
        print(s[i].lower(), end = '')