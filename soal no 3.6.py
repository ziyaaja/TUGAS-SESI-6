row = 5
col = 5
for i in range(1, row + 1):
    for j in range(i, i + col):
        print(j * 2 - 1, end=" ")
    print()
