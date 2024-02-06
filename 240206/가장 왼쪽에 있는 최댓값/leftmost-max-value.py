n = int(input())
a = list(map(int, input().split()))
while len(a) != 0:
    print(a.index(max(a))+1, end = ' ')
    a = a[:a.index(max(a))]