import time
import sys

def typewriter(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# ===== CLIENT GREETING =====
name = input("What is your name --> ")
typewriter(f"Hello, {name}! Welcome to my finals, hope you learn today here!", speed=0.05)

time.sleep(2)
start_program = input("Do you want to start? (Yes or No) ")

if start_program.lower() == "yes":

    # ===== PRINTING MENU =====
    def printing_menu():
        while True:
            

            print("\n--- PRINTING IN PYTHON MENU ---")
            print("1. Simple Printing Examples")
            print("2. String Concatenation Examples")
            print("3. Try It Yourself")
            print("4. Back to Main Menu")

            choice = input("Choose an option: ")

            if choice == "1":
                print("=======================================================")
                typewriter("Printing in Python is the process of sending information from a program to the screen so the user can see it.", speed= 0.03)
                print("======================================================= \n")                
                print("\n ----SIMPLE PRINTING EXAMPLE----")
                print("print('Hello World')  # prints a string")
                print("output:")
                print("Hello World\n")
                print("print(123)  # prints a number")
                print("output:")
                print("123\n")
                print("print('Name:', 'Kyky')  # prints multiple values separated by space and comma")
                print("output:")
                print(name," and (kyky) if s a user input kyky in a variable\n")
                
                time.sleep(2)
 
            elif choice == "2":

                print("=======================================================")
                typewriter("String concatenation in Python means joining two or more strings together to make a single string.", speed= 0.03)
                print("======================================================= \n")  
                print("\n>>> STRING CONCATENATION EXAMPLE")               
                print("name = 'Kyky'  # storing a string")
                print("output")
                print("if you put the name in a print function, then it will show you not the word name, but the variable like kyky, or like the one you put in your name", name,"\n")
                print("print('Hello ' + name)  # combining strings (concatenation)")
                print("output:")
                print("Hello", name,"\n")
                print("print('Age: ' + str(18))  # converting number to string for concatenation\n")
                print("output:")
                print("So 'age ' + str(18) combines age and 18 to form:")
                print("Age 18\n")

                typewriter("PRESS anything once you have READ nd UNDERSTOOD this String Concantenation", speed= 0.03)
                gets= input()
                
                
                time.sleep(2)

            elif choice == "3":
                print("\n>>> TRY PRINTING YOURSELF")
                user_text = input("Type anything you want to print: ")
                print("Your Output:")
                print(user_text, " # this is what you entered printed on screen\n")

            elif choice == "4":
                break
            else:
                print("Invalid choice. Try again.\n")


    # ===== VARIABLES MENU =====
    def variables_menu():
        while True:
            print("\n--- VARIABLES MENU ---")
            print("1. Variable Examples")
            print("2. Changing Values")
            print("3. Try It Yourself")
            print("4. Back to Main Menu")

            choice = input("Choose an option: ")

            if choice == "1":
                print("\n>>> BASIC VARIABLE EXAMPLE")
                print("name = 'Kyky'  # variable storing a string")
                print("age = 18  # variable storing a number")
                print("print(name, age)  # prints both variable values\n")

            elif choice == "2":
                print("\n>>> CHANGING VARIABLE VALUES")
                print("x = 10  # initial value")
                print("x = 20  # updated value")
                print("print(x)  # prints 20 because x was reassigned\n")

            elif choice == "3":
                print("\n>>> TRY VARIABLES YOURSELF")
                var_name = input("Enter variable name: ")
                var_value = input("Enter variable value: ")
                print("\nYour variable created:")
                print(var_name, "=", var_value, " # you assigned a value to a variable\n")

            elif choice == "4":
                break
            else:
                print("Invalid choice.\n")


    # ===== CONDITIONAL MENU =====
    def conditionals_menu():
        while True:
            print("\n--- CONDITIONAL STATEMENTS MENU ---")
            print("1. Simple If Example")
            print("2. If-Else Example")
            print("3. Try It Yourself")
            print("4. Back to Main Menu")

            choice = input("Choose an option: ")

            if choice == "1":
                print("\n>>> SIMPLE IF")
                print("num = 10  # storing a value")
                print("if num > 5:  # condition checks if number is greater than 5")
                print("    print('Number is greater than 5')  # printed because condition is TRUE\n")

            elif choice == "2":
                print("\n>>> IF-ELSE")
                print("age = 16  # storing age")
                print("if age >= 18:  # checks if adult")
                print("    print('Adult')")
                print("else:")
                print("    print('Minor')  # printed because age is less than 18\n")

            elif choice == "3":
                print("\n>>> TRY CONDITIONALS")
                number = int(input("Enter a number: "))
                print("Your result:")
                if number > 0:
                    print("Positive number!  # number is greater than zero\n")
                elif number < 0:
                    print("Negative number!  # number is less than zero\n")
                else:
                    print("Zero!  # number is exactly zero\n")

            elif choice == "4":
                break
            else:
                print("Invalid choice.\n")


    # ===== LOOPING MENU =====
    def looping_menu():
        while True:
            print("\n--- LOOPING MENU ---")
            print("1. For Loop Example")
            print("2. While Loop Example")
            print("3. Try It Yourself")
            print("4. Back to Main Menu")

            choice = input("Choose an option: ")

            if choice == "1":
                print("\n>>> FOR LOOP")
                print("for i in range(5):  # loop from 0 to 4")
                print("    print(i)  # prints each number in the loop\n")

            elif choice == "2":
                print("\n>>> WHILE LOOP")
                print("count = 1  # starting value")
                print("while count <= 5:  # loop runs while condition is TRUE")
                print("    print(count)  # prints current count")
                print("    count += 1  # increases value to avoid infinite loop\n")

            elif choice == "3":
                print("\n>>> TRY LOOPING")
                end = int(input("Enter a number to loop to: "))
                print("Your loop:")
                for i in range(1, end + 1):
                    print(i, " # printed because loop repeats until your number")
                print("")

            elif choice == "4":
                break
            else:
                print("Invalid choice.\n")


    # ===== FUNCTIONS MENU =====
    def functions_menu():
        while True:
            print("\n--- FUNCTIONS MENU ---")
            print("1. Simple Function Example")
            print("2. Function with Parameter Example")
            print("3. Try It Yourself")
            print("4. Back to Main Menu")

            choice = input("Choose an option: ")

            if choice == "1":
                print("\n>>> SIMPLE FUNCTION")
                print("def greet():  # function definition")
                print("    print('Hello!')  # executed when function is called")
                print("greet()  # calling the function prints the message\n")

            elif choice == "2":
                print("\n>>> FUNCTION WITH PARAMETER")
                print("def greet(name):  # function that accepts input")
                print("    print('Hello ' + name)")
                print("greet('Kyky')  # passes a value to the function\n")

            elif choice == "3":
                print("\n>>> TRY FUNCTION")
                user_name = input("Enter a name: ")
                print("Function Output:")
                print("Hello", user_name, " # printed using your input\n")

            elif choice == "4":
                break
            else:
                print("Invalid choice.\n")


    # ===== ARRAYS / LISTS MENU =====
    def arrays_menu():
        while True:
            print("\n--- ARRAYS / LISTS MENU ---")
            print("1. Basic List Example")
            print("2. Append Example")
            print("3. Try It Yourself")
            print("4. Back to Main Menu")

            choice = input("Choose an option: ")

            if choice == "1":
                print("\n>>> BASIC LIST")
                print("fruits = ['apple', 'banana', 'mango']  # list of strings")
                print("print(fruits)  # prints entire list\n")

            elif choice == "2":
                print("\n>>> APPEND EXAMPLE")
                print("numbers = [1, 2, 3]  # initial list")
                print("numbers.append(4)  # adds new value at the end")
                print("print(numbers)  # prints updated list [1, 2, 3, 4]\n")

            elif choice == "3":
                print("\n>>> TRY LIST")
                my_list = []
                item = input("Add an item to a list: ")
                my_list.append(item)
                print("Your list:", my_list, " # your item was added to the list\n")

            elif choice == "4":
                break
            else:
                print("Invalid choice.\n")


    # ===== DICTIONARY MENU =====
    def dictionary_menu():
        while True:
            print("\n--- DICTIONARY MENU ---")
            print("1. Basic Dictionary Example")
            print("2. Update Value Example")
            print("3. Try It Yourself")
            print("4. Back to Main Menu")

            choice = input("Choose an option: ")

            if choice == "1":
                print("\n>>> BASIC DICTIONARY")
                print("person = {'name': 'Kyky', 'age': 18}  # key-value pairs")
                print("print(person)  # prints entire dictionary\n")

            elif choice == "2":
                print("\n>>> UPDATE VALUE")
                print("person = {'name': 'Kyky', 'age': 18}")
                print("person['age'] = 19  # updates value")
                print("print(person)  # prints updated dictionary\n")

            elif choice == "3":
                print("\n>>> TRY DICTIONARY")
                key = input("Enter key: ")
                value = input("Enter value: ")
                user_dict = {}
                user_dict[key] = value
                print("Your dictionary:", user_dict, " # you created a dictionary entry\n")

            elif choice == "4":
                break
            else:
                print("Invalid choice.\n")


    # ===== MAIN MENU =====
    while True:
        print("\n===== PYTHON LESSON MAIN MENU =====")
        print("1. Printing")
        print("2. Variables")
        print("3. Conditionals")
        print("4. Loops")
        print("5. Functions")
        print("6. Arrays / Lists")
        print("7. Dictionary")
        print("8. Exit")

        main_choice = input("Enter your choice: ")

        if main_choice == "1":
            printing_menu()
        elif main_choice == "2":
            variables_menu()
        elif main_choice == "3":
            conditionals_menu()
        elif main_choice == "4":
            looping_menu()
        elif main_choice == "5":
            functions_menu()
        elif main_choice == "6":
            arrays_menu()
        elif main_choice == "7":
            dictionary_menu()
        elif main_choice == "8":
            print("Goodbye,", name + "!")
            break
        else:
            print("Invalid choice. Try again.\n")

else:
    print("Program ended.")
    