def printing_in_python():
    print("\n--- PRINTING IN PYTHON ---")
    print("To print in Python, use the print() function.")
    print("Example:")
    print("print('Hello World')\n")

def variables_in_python():
    print("\n--- VARIABLES IN PYTHON ---")
    print("Variables store data. No need for type declaration in Python.")
    print("Example:")
    print("name = 'Kyky'")
    print("age = 18\n")

def conditional_statements():
    print("\n--- CONDITIONAL STATEMENTS ---")
    print("Use if, elif, else to make decisions.")
    print("Example:")
    print("if age >= 18:")
    print("    print('Adult')\n")

def looping_statements():
    print("\n--- LOOPING STATEMENTS ---")
    print("for loop and while loop are commonly used.")
    print("Example:")
    print("for i in range(5):")
    print("    print(i)\n")

def functions():
    print("\n--- FUNCTIONS IN PYTHON ---")
    print("Functions are reusable blocks of code.")
    print("Example:")
    print("def greet():")
    print("    print('Hello!')")
    print("greet()\n")

def arrays_lists():
    print("\n--- ARRAYS / LISTS IN PYTHON ---")
    print("Python uses LISTS to store multiple values.")
    print("Example:")
    print("fruits = ['apple', 'banana', 'mango']")
    print("print(fruits[0])\n")

def dictionary():
    print("\n--- DICTIONARY IN PYTHON ---")
    print("Dictionaries store key-value pairs.")
    print("Example:")
    print("person = {'name': 'Kyky', 'age': 18}")
    print("print(person['name'])\n")


# ===== MAIN PROGRAM USING WHILE LOOP =====
choice = 0

while choice != 8:
    print("===== PYTHON LESSON MENU =====")
    print("1. Printing in Python")
    print("2. Variables in Python")
    print("3. Conditional Statements")
    print("4. Looping Statements")
    print("5. Functions")
    print("6. Arrays / Lists")
    print("7. Dictionary")
    print("8. Exit")

    choice = int(input("Enter your choice (1-8): "))

    if choice == 1:
        printing_in_python()
    elif choice == 2:
        variables_in_python()
    elif choice == 3:
        conditional_statements()
    elif choice == 4:
        looping_statements()
    elif choice == 5:
        functions()
    elif choice == 6:
        arrays_lists()
    elif choice == 7:
        dictionary()
    elif choice == 8:
        print("Exiting program... Goodbye!")
    else:
        print("Invalid choice! Please choose 1–8.\n")
