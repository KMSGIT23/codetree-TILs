n = int(input())
a = list(map(int, input().split()))
b = []
for i in a:
    b.append(i)
    if i >= 100:
        break
print(sum(b))
print("%.1f"%(sum(b) / len(b)))