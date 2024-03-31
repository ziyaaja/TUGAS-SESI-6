def print_pattern(length):
    for i in range(length):
        for j in range(length):
            if (i + j) % 2 == 0:
                print("A", end=" ")
            else:
                print("B", end=" ")
        print()

length = 5 
print_pattern(length)
