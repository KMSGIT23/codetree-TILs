n = int(input())
for i in range(n):
    c = input()
    try:
        print(chr(int(c)))
    except:
        print(ord(c))