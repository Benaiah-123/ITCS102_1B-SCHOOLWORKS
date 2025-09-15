print ("The Factorial program")

number = eval(input("enter any amount here--> "))
factorial = 1
for x in range(number, 0, -1):
    factorial *= x
print("the factorial of", number, "is", factorial)