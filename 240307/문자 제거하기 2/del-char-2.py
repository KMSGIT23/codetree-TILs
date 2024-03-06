s, n = input().split(); n = int(n)
for i in range(n):
    r = int(input())
    if r <= len(s):
        s = s[:r-1] + s[r:]
        print(s)