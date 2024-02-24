n = int(input())
a = list(map(int, input().split()))
p, q = map(int, input().split())
print("%.1f"%((a[p-1]+a[q-1]) / 2))