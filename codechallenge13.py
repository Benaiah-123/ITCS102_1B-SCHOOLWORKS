
name = input("input the name here --> ")
print(" +++++++++++++++++++++++++++++++++++++ ")
print(" Odd number sumaation, pres 0 to stop")
print(" +++++++++++++++++++++++++++++++++++++ ")

lols= True
sum = 0
odd = ""

while lols == True:
    num = eval(input("eenter your number here --> "))

    if num % 2 ==1:
        print("odd number detected, code continues")
        sum += num
        odd += str(num) + "2"
        continue
    elif num % 2 ==0:
        print("code stops")
        break

    else:
        if num % 2== 0:
            print("Even number detected, code continues")
        else:
            print("invalid")
            continue

print(f"hi {name}, the sum of all odd number is, {sum}")
print(f"odd numbers detected included the ff {odd}")
     