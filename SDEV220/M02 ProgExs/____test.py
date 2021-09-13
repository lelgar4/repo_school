n = int(input("Enter number of lines: "))
x = n * 2
for i in range(1, n + 1):
    s = n + x
    sp = str(s) + "s"
    print(format(" ", sp), end='')
    for j in range(i, 0, -1):
        print(j, end='  ')
    for j in range(2, i + 1):
        print(j, end='  ')

    print(format(" ", sp))
    x -= 3