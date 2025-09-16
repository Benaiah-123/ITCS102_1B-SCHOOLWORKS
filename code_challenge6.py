print("Odd number summation")
sum = 0
for y in range (1, 11, 1):
    number= eval(input("enter any number here--> "))
    if number % 2 != 0:
        print (y, "is odd")
        sum += number
   

print(sum, "these are the odds!")
