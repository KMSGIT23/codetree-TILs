n = int(input())
a = list(map(int, input().split()))
seven = []
for i in a:
    if i % 7 == 0:
        seven.append(i)
print(len(seven), sum(seven), "%.1f"%(sum(seven) / len(seven)))