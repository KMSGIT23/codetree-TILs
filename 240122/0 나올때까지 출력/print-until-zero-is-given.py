last = []

while True:
    try:
        n = int(input())
        if n != 0:
            last.append(n)
        else:
            break  # Exit the loop when n is 0
    except EOFError:
        break  # Exit the loop if EOFError occurs (end of input)

for i in last:
    print(i)