# ---------- SUB-MENUS ----------
name = input("what is your name --> ")
print ("Hello, welcome to my finals in itcs102," ,name)
start_program = input("do you want to start, (Yes or No)  ")

if start_program.lower() == 'yes':
    def printing_menu():
        while True:
            print("\n--- PRINTING IN PYTHON MENU ---")
            print("1. Simple Printing")
            print("2. Printing with String Concatenation")
            print("3. Back to Main Menu")

            choice = input("Choose an option: ")

            if choice == "1":
                print("\n>>> SIMPLE PRINTING EXAMPLE")
                print("print('Hello World')")
                print("print(123)")
                print("print('Name:', 'Kyky')\n")

            elif choice == "2":
                print("\n>>> STRING CONCATENATION PRINTING")
                print("name = 'Kyky'")
                print("print('Hello ' + name)")
                print("print('Age: ' + str(18))\n")

            elif choice == "3":
                break
            else:
                print("Invalid choice. Try again.\n")


    def variables_menu():
        while True:
            print("\n--- VARIABLES MENU ---")
            print("1. Basic Variable Example")
            print("2. Changing Variable Value")
            print("3. Back to Main Menu")

            choice = input("Choose an option: ")

            if choice == "1":
                print("\n>>> BASIC VARIABLE EXAMPLE")
                print("name = 'Kyky'")
                print("age = 18")
                print("print(name, age)\n")

            elif choice == "2":
                print("\n>>> CHANGING VARIABLE VALUES")
                print("x = 10")
                print("x = 20  # now x becomes 20")
                print("print(x)\n")

            elif choice == "3":
                break
            else:
                print("Invalid choice.\n")


    def conditionals_menu():
        while True:
            print("\n--- CONDITIONALS MENU ---")
            print("1. Simple If")
            print("2. If-Else Example")
            print("3. Back to Main Menu")

            choice = input("Choose an option: ")

            if choice == "1":
                print("\n>>> SIMPLE IF")
                print("num = 10")
                print("if num > 5:")
                print("    print('Number is greater than 5')\n")

            elif choice == "2":
                print("\n>>> IF-ELSE")
                print("age = 16")
                print("if age >= 18:")
                print("    print('Adult')")
                print("else:")
                print("    print('Minor')\n")

            elif choice == "3":
                break
            else:
                print("Invalid choice.\n")


    def looping_menu():
        while True:
            print("\n--- LOOPING MENU ---")
            print("1. For Loop Example")
            print("2. While Loop Example")
            print("3. Back to Main Menu")

            choice = input("Choose an option: ")

            if choice == "1":
                print("\n>>> FOR LOOP")
                print("for i in range(5):")
                print("    print(i)\n")

            elif choice == "2":
                print("\n>>> WHILE LOOP")
                print("count = 1")
                print("while count <= 5:")
                print("    print(count)")
                print("    count += 1\n")

            elif choice == "3":
                break
            else:
                print("Invalid choice.\n")


    def functions_menu():
        while True:
            print("\n--- FUNCTIONS MENU ---")
            print("1. Creating a Function")
            print("2. Function with Parameters")
            print("3. Back to Main Menu")

            choice = input("Choose an option: ")

            if choice == "1":
                print("\n>>> SIMPLE FUNCTION")
                print("def greet():")
                print("    print('Hello!')")
                print("greet()\n")

            elif choice == "2":
                print("\n>>> FUNCTION WITH PARAMETERS")
                print("def greet(name):")
                print("    print('Hello ' + name)")
                print("greet('Kyky')\n")

            elif choice == "3":
                break
            else:
                print("Invalid choice.\n")


    def arrays_menu():
        while True:
            print("\n--- ARRAYS / LISTS MENU ---")
            print("1. Basic List Example")
            print("2. Adding Items to List")
            print("3. Back to Main Menu")

            choice = input("Choose an option: ")

            if choice == "1":
                print("\n>>> BASIC LIST")
                print("fruits = ['apple', 'banana', 'mango']")
                print("print(fruits)\n")

            elif choice == "2":
                print("\n>>> APPEND TO LIST")
                print("numbers = [1, 2, 3]")
                print("numbers.append(4)")
                print("print(numbers)\n")

            elif choice == "3":
                break
            else:
                print("Invalid choice.\n")


    def dictionary_menu():
        while True:
            print("\n--- DICTIONARY MENU ---")
            print("1. Basic Dictionary")
            print("2. Updating Dictionary")
            print("3. Back to Main Menu")

            choice = input("Choose an option: ")

            if choice == "1":
                print("\n>>> BASIC DICTIONARY")
                print("person = {'name': 'Kyky', 'age': 18}")
                print("print(person)\n")

            elif choice == "2":
                print("\n>>> UPDATE VALUE")
                print("person = {'name': 'Kyky', 'age': 18}")
                print("person['age'] = 19")
                print("print(person)\n")

            elif choice == "3":
                break
            else:
                print("Invalid choice.\n")


    # ---------- MAIN MENU LOOP ----------
    while True:
        print("\n===== PYTHON LESSON MAIN MENU =====")
        print("1. Printing in Python")
        print("2. Variables in Python")
        print("3. Conditional Statements")
        print("4. Looping Statements")
        print("5. Functions")
        print("6. Arrays / Lists")
        print("7. Dictionary")
        print("8. Exit")

        main_choice = input("Enter your choice (1-8): ")

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
            print("Exiting program... Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")
