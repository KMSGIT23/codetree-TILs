w = list(input())
w.remove(w[1])
e = w[-1]
w.pop()
w.pop()
w.append(e)
w = ''.join(w)
print(w)