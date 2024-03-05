s = ''
n = int(input())
for i in range(n):
    c = input()
    s += c
print(s[:len(s)//2])
print(s[len(s)//2:])