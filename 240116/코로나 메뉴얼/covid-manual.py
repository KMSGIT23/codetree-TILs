e = 0
for i in range(3):
    a, b = input().split()
    if a == 'Y' and int(b) >= 37:
        e += 1
print("E" if e >= 2 else "N")