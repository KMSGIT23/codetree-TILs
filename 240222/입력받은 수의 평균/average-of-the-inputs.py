n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
print("%.1f"%(sum(a) / len(a)))