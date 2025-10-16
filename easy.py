for i in range(1, 7, 1):
    for j in range(1, i+1, 1):
        print(i, end=" ")
    print()

for i in range(1, 7, 1):
    for k in range(7, i, -1):
        print(" ", end=" ")
    for j in range(1, i*2, 1):
        print("*", end=" ")
    print()
