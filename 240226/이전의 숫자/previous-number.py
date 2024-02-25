n = int(input())
a = list(map(int, input().split()))
print(sum(a[a.index(0)-5:a.index(0)]))