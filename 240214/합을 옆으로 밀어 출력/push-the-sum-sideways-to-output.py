n = int(input()); a = []
for i in range(n):
    a.append(int(input()))
a = str(sum(a))
print(a[1:] + a[0])