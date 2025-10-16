for i in range(1, 7, 1):
    for k in range(7, i, -1):
        print(" ", end="")
    for j in range(1, i+1, 1):
        print("* ", end="")
    print()

user = eval(input("Enter a number: "))

for i in range(1, 11, 1):
    for k in range(1, user + 1, 1):
        print(i, "x", k, "=", i * k, end="\t")
    print()