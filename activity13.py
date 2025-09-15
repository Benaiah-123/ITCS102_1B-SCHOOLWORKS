#let the user input 20 variables
#get the summation of all variables
sum = 0
for I in range (1, 21, 1):
    print(I)
    n2 = eval(input("enter any numbers here->  "))
    sum += n2

print("the sum of all number is", sum)
    