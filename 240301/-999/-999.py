a = list(map(int, input().split()))
del a[-1]
print(max(a), min(a))