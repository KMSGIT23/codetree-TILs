a = input()
ee, eb = 0, 0
for i in range(2, len(a)+2):
    if a[i-2:i] == 'ee':
        ee += 1
    elif a[i-2:i] == 'eb':
        eb += 1
    else:
        continue
print(ee, eb)