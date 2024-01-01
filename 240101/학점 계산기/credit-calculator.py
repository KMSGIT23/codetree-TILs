n = int(input())
a = list(map(float, input().split()))
b = sum(a) / n
if b > 3.9:
    print("%.1f"%b)
    print("Perfect")
elif b > 2.9:
    print("%.1f"%b)
    print("Good")
else:
    print("%.1f"%b)
    print("Poor")