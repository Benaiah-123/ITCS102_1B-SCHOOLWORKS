import time
import sys
import os
import json

# ---------------------------
# Utilities: typewriter, loading, separators, safe input
# ---------------------------

def typewriter(text, speed=0.025):
    """Print text with a typewriter effect (adjust speed)."""
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def loading_dots(times=3, delay=0.6):
    """Simple loading dots animation."""
    print("Loading", end="", flush=True)
    for _ in range(times):
        print(".", end="", flush=True)
        time.sleep(delay)
    print()

def separator(char="=", length=60):
    print(char * length)

def banner(title):
    separator("=" , 70)
    typewriter(f"    ✨ {title} ✨", speed=0.01)
    separator("=" , 70)

def press_to_continue(prompt="Press Enter to continue..."):
    try:
        input(prompt)
    except (KeyboardInterrupt, EOFError):
        print()
        return

def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def safe_int_input(prompt, default=None):
    """Convert input to int safely; returns default if empty and default provided."""
    while True:
        val = input(prompt)
        if val.strip() == "" and default is not None:
            return default
        try:
            return int(val)
        except ValueError:
            print("Please enter a valid integer.")

def safe_float_input(prompt, default=None):
    while True:
        val = input(prompt)
        if val.strip() == "" and default is not None:
            return default
        try:
            return float(val)
        except ValueError:
            print("Please enter a valid number.")

# ---------------------------
# Persistence (optional): simple save/load progress
# ---------------------------

SAVE_FILE = "itcs102_progress.json"

def save_progress(progress):
    try:
        with open(SAVE_FILE, "w") as f:
            json.dump(progress, f, indent=2)
        print("(Progress saved.)")
    except Exception:
        print("(Could not save progress.)")

def load_progress():
    try:
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, "r") as f:
                return json.load(f)
    except Exception:
        pass
    return {}

# ---------------------------
# Common UI building blocks (consistent with printing_menu style)
# ---------------------------

def lesson_header(title):
    clear_screen()
    banner(title)

def lesson_footer():
    separator("-", 60)
    press_to_continue("Press Enter when you've read and understood this lesson... ")
    loading_dots()
    time.sleep(0.4)

# ---------------------------
# Modules (each upgraded to match printing_menu style)
# ---------------------------

def printing_menu(state):
    """Upgraded printing menu with typewriter explanation, separators, loading, and confirmations."""
    while True:
        lesson_header("PRINTING IN PYTHON")
        print("This module covers how Python prints information to the screen using the print() function.")
        print()
        print("1. Simple Printing Examples")
        print("2. String Concatenation Examples")
        print("3. Formatted Printing (f-strings)")
        print("4. Try Printing Yourself")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            separator()
            # Detailed explanation via typewriter
            typewriter("Printing in Python is the process of sending information from a program to the screen so the user can see it.", speed=0.03)
            separator()
            print()
            print("---- SIMPLE PRINTING EXAMPLES ----")
            print("print('Hello World')    # prints a string to the screen")
            print("output:")
            print("Hello World")
            print()
            print("print(123)              # prints a number (integers printed as-is)")
            print("output:")
            print(123)
            print()
            print("print('Name:', name)    # prints label and value, separated by space automatically")
            print("output (example if name='Kyky'):")
            print("Name: ", state.get("name_example", "Kyky"))
            lesson_footer()

        elif choice == "2":
            separator()
            typewriter("String concatenation in Python means joining two or more strings together to make a single string.", speed=0.03)
            separator()
            print()
            print("---- STRING CONCATENATION ----")
            print("name = 'Kyky'           # storing a string in the variable name")
            print("print('Hello ' + name)  # combining strings using the + operator")
            print("output (example):")
            print("Hello " + state.get("name_example", "Kyky"))
            print()
            print("print('Age: ' + str(18))  # converting number to string using str() before concatenation")
            print("output:")
            print("Age: " + str(18))
            lesson_footer()

        elif choice == "3":
            separator()
            typewriter("Formatted printing (f-strings) lets you insert variables directly into string literals, which is both readable and efficient.", speed=0.03)
            separator()
            print()
            print("---- FORMATTED PRINTING (f-strings) ----")
            print("name = 'Kyky'")
            print("age = 18")
            print("print(f'Name: {name}, Age: {age}')  # f-string inserts variables into the string")
            print("output (example):")
            print(f"Name: {state.get('name_example', 'Kyky')}, Age: {state.get('age_example', 18)}")
            lesson_footer()

        elif choice == "4":
            separator()
            typewriter("Try it yourself: type anything and the program will print it back. You can also try a simple arithmetic expression to see evaluation.", speed=0.03)
            separator()
            print("\n---- TRY PRINTING YOURSELF ----")
            user_text = input("Type anything you want to print: ")
            print("\nYour Output:")
            print(user_text, "  # this is what you entered printed on screen")
            print()
            expr_try = input("Optional: Enter a simple arithmetic expression to evaluate (e.g. 2+3), or press Enter to skip: ")
            if expr_try.strip():
                # Basic safe check before eval: allow numbers, spaces, and math operators only
                allowed = set("0123456789+-*/(). ")
                if set(expr_try) <= allowed:
                    try:
                        result = eval(expr_try)
                        print("Evaluation result:", result)
                        print("# This shows the arithmetic expression computed by Python.")
                    except Exception as e:
                        print("Could not evaluate expression:", e)
                else:
                    print("Expression contains invalid characters; only simple arithmetic is allowed here.")
            print()
            press_to_continue("Press Enter to continue (you can try again selecting option 4)... ")
            loading_dots()
            time.sleep(0.3)

        elif choice == "5":
            typewriter("Going back to main menu...", speed=0.03)
            loading_dots()
            break
        else:
            print("Invalid choice. Try again.")
            time.sleep(0.4)


def variables_menu(state):
    while True:
        lesson_header("VARIABLES IN PYTHON")
        print("Variables are used to store data. Python is dynamically typed, so you don't declare types explicitly.")
        print()
        print("1. Basic Variable Examples")
        print("2. Changing Values (Reassignment)")
        print("3. Data Types Explanation")
        print("4. Try Variables Yourself")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            separator()
            typewriter("Variables hold values that your program can use later. You give variables descriptive names.", speed=0.03)
            separator()
            print()
            print("---- BASIC VARIABLE EXAMPLES ----")
            print("name = 'Kyky'      # variable storing a string")
            print("age = 18           # variable storing an integer")
            print("pi = 3.14          # floating point number")
            print("is_student = True  # boolean value (True/False)")
            print()
            print("print(name, age)   # prints both variable values separated by space")
            print("output (example):")
            print(state.get("name_example", "Kyky"), state.get("age_example", 18))
            lesson_footer()

        elif choice == "2":
            separator()
            typewriter("You can change a variable's value at any time by assigning a new value to the same name. This is called reassignment.", speed=0.03)
            separator()
            print()
            print("---- CHANGING VARIABLE VALUES ----")
            print("x = 10      # assigns initial value 10 to x")
            print("x = 20      # reassigns x now to 20")
            print("print(x)    # prints current value of x, which is 20")
            print("output:")
            print(20)
            lesson_footer()

        elif choice == "3":
            separator()
            typewriter("Common built-in data types: int (integers), float (decimals), str (strings), bool (True/False). Use type() to see the type.", speed=0.03)
            separator()
            print()
            print("---- DATA TYPES ----")
            print("print(type(10))    # shows <class 'int'>")
            print("print(type(3.14))  # shows <class 'float'>")
            print("print(type('hi'))  # shows <class 'str'>")
            print("print(type(True))  # shows <class 'bool'>")
            lesson_footer()

        elif choice == "4":
            separator()
            typewriter("Try creating a variable yourself. Enter the variable name and a value; we'll display the simulated assignment and printed value.", speed=0.03)
            separator()
            print("\n---- TRY VARIABLES YOURSELF ----")
            var_name = input("Enter variable name (letters and underscore only recommended): ").strip()
            if not var_name:
                var_name = "my_var"
            var_value = input("Enter variable value (we'll treat it as a string for demonstration): ").strip()
            print()
            print("Simulated code:")
            print(f"{var_name} = '{var_value}'")
            print("Then printing that variable would show:")
            print(var_value, f"  # the value assigned to {var_name}")
            # store example in state for demos
            state["last_var_name"] = var_name
            state["last_var_value"] = var_value
            lesson_footer()

        elif choice == "5":
            typewriter("Going back to main menu...", speed=0.03)
            loading_dots()
            break
        else:
            print("Invalid choice. Try again.")
            time.sleep(0.3)


def conditionals_menu(state):
    while True:
        lesson_header("CONDITIONAL STATEMENTS (if / else / elif)")
        print("Conditionals allow your program to make decisions based on data.")
        print()
        print("1. Simple if Example")
        print("2. If-Else and Elif Example")
        print("3. Try Conditionals (positive/negative/zero)")
        print("4. Mini Explanation: Boolean logic")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            separator()
            typewriter("An if statement runs a block of code only when the condition is True.", speed=0.03)
            separator()
            print()
            print("---- SIMPLE IF ----")
            print("num = 10")
            print("if num > 5:            # checks if 10 is greater than 5")
            print("    print('Number is greater than 5')  # this will run because condition is True")
            print("output:")
            print("Number is greater than 5")
            lesson_footer()

        elif choice == "2":
            separator()
            typewriter("Use if-elif-else to check multiple conditions in order. The first condition that is True runs and the rest are skipped.", speed=0.03)
            separator()
            print()
            print("---- IF-ELSE / ELIF ----")
            print("age = 16")
            print("if age >= 18:")
            print("    print('Adult')")
            print("elif age >= 13:")
            print("    print('Teen')")
            print("else:")
            print("    print('Child')")
            print("output (for age=16):")
            print("Teen")
            lesson_footer()

        elif choice == "3":
            separator()
            typewriter("Try entering a number; the program will tell you if it is positive, negative, or zero.", speed=0.03)
            separator()
            print()
            print("---- TRY CONDITIONALS ----")
            try:
                number = int(input("Enter an integer: "))
            except ValueError:
                print("That's not an integer. Returning to conditionals menu.")
                time.sleep(0.6)
                continue
            print("Your result:")
            if number > 0:
                print("Positive number!  # number is greater than zero")
            elif number < 0:
                print("Negative number!  # number is less than zero")
            else:
                print("Zero!  # number is exactly zero")
            press_to_continue()
            loading_dots()
            time.sleep(0.3)

        elif choice == "4":
            separator()
            typewriter("Boolean values (True / False) are used to evaluate conditions. Comparisons like >, <, == produce boolean results.", speed=0.03)
            separator()
            print()
            print("---- BOOLEAN LOGIC ----")
            print("print(5 > 3)   # True")
            print("print(5 == 3)  # False")
            print("print(5 != 3)  # True")
            lesson_footer()

        elif choice == "5":
            typewriter("Going back to main menu...", speed=0.03)
            loading_dots()
            break
        else:
            print("Invalid choice. Try again.")
            time.sleep(0.3)


def operators_menu(state):
    while True:
        lesson_header("OPERATORS IN PYTHON")
        typewriter("Operators let you perform arithmetic, comparisons, logic, and assignment operations on values and variables.", speed=0.03)
        print()
        print("1. Arithmetic Operators (+, -, *, /, %, **, //)")
        print("2. Comparison Operators (==, !=, >, <, >=, <=)")
        print("3. Logical Operators (and, or, not)")
        print("4. Assignment Operators (+=, -=, *=, etc.)")
        print("5. Try Operators (enter two numbers)")
        print("6. Back to Main Menu")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            separator()
            typewriter("Arithmetic operators perform mathematical operations.", speed=0.03)
            separator()
            print()
            print("a = 10")
            print("b = 3")
            print("print(a + b)  # Addition => 13")
            print("print(a - b)  # Subtraction => 7")
            print("print(a * b)  # Multiplication => 30")
            print("print(a / b)  # True division => 3.3333333333333335")
            print("print(a % b)  # Modulus (remainder) => 1")
            print("print(a ** b) # Exponent (power) => 1000")
            print("print(a // b) # Floor division => 3")
            lesson_footer()

        elif choice == "2":
            separator()
            typewriter("Comparison operators compare values and return True or False.", speed=0.03)
            separator()
            print()
            print("x = 5")
            print("y = 10")
            print("print(x == y)  # Equal => False")
            print("print(x != y)  # Not equal => True")
            print("print(x > y)   # Greater than => False")
            print("print(x < y)   # Less than => True")
            print("print(x >= y)  # Greater or equal => False")
            print("print(x <= y)  # Less or equal => True")
            lesson_footer()

        elif choice == "3":
            separator()
            typewriter("Logical operators combine boolean expressions.", speed=0.03)
            separator()
            print()
            print("p = True")
            print("q = False")
            print("print(p and q)  # AND => False (both must be True)")
            print("print(p or q)   # OR => True (at least one True)")
            print("print(not p)    # NOT => False (inverts boolean)")
            lesson_footer()

        elif choice == "4":
            separator()
            typewriter("Assignment operators update variables in place.", speed=0.03)
            separator()
            print()
            print("x = 10       # simple assignment")
            print("x += 5       # x = x + 5")
            print("x -= 3       # x = x - 3")
            print("x *= 2       # x = x * 2")
            print("x /= 4       # x = x / 4 (becomes float)")
            print("x %= 2       # x = x % 2")
            print("x **= 3      # x = x ** 3")
            print("x //= 2      # x = x // 2 (floor division)")
            lesson_footer()

        elif choice == "5":
            separator()
            typewriter("Try operators with two numbers. We'll show common results for demonstration.", speed=0.03)
            separator()
            num1 = safe_float_input("Enter first number: ")
            num2 = safe_float_input("Enter second number: ")
            print()
            print("Addition:", num1 + num2)
            print("Subtraction:", num1 - num2)
            print("Multiplication:", num1 * num2)
            if num2 != 0:
                print("Division:", num1 / num2)
                print("Modulus:", num1 % num2)
                print("Floor division:", num1 // num2)
            else:
                print("Division and modulus: cannot divide by zero.")
            print("Exponent:", num1 ** num2)
            press_to_continue()
            loading_dots()
            time.sleep(0.3)

        elif choice == "6":
            typewriter("Going back to main menu...", speed=0.03)
            loading_dots()
            break
        else:
            print("Invalid choice. Try again.")
            time.sleep(0.3)


def loops_menu(state):
    while True:
        lesson_header("LOOPS (FOR & WHILE)")
        typewriter("Loops allow you to repeat code multiple times. Use 'for' for a known number of iterations and 'while' when a condition controls repetition.", speed=0.03)
        print()
        print("1. For Loop Example")
        print("2. While Loop Example")
        print("3. Try Loops Yourself")
        print("4. Loop Control (break / continue)")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            separator()
            print("---- FOR LOOP ----")
            print("for i in range(5):    # range(5) produces 0,1,2,3,4")
            print("    print(i)          # prints each value from 0 to 4")
            print("output:")
            for i in range(5):
                print(i)
            lesson_footer()

        elif choice == "2":
            separator()
            print("---- WHILE LOOP ----")
            print("count = 1")
            print("while count <= 5:     # runs until condition becomes False")
            print("    print(count)")
            print("    count += 1")
            print("output:")
            count = 1
            while count <= 5:
                print(count)
                count += 1
            lesson_footer()

        elif choice == "3":
            separator()
            typewriter("Enter a number and we'll print numbers from 1 up to that number using a loop.", speed=0.03)
            separator()
            n = safe_int_input("Print numbers from 1 to: ", default=5)
            print("Your loop output:")
            for i in range(1, n + 1):
                print(i, "# printed by the loop")
            press_to_continue()
            loading_dots()
            time.sleep(0.3)

        elif choice == "4":
            separator()
            typewriter("The 'break' statement exits the current loop; 'continue' skips the rest of the current iteration and proceeds to the next.", speed=0.03)
            separator()
            print()
            print("Example with break:")
            for i in range(1, 6):
                if i == 4:
                    print("break encountered at", i)
                    break
                print("i =", i)
            print()
            print("Example with continue:")
            for i in range(1, 6):
                if i == 3:
                    print("continue at", i, "(skipping this iteration)")
                    continue
                print("i =", i)
            lesson_footer()

        elif choice == "5":
            typewriter("Going back to main menu...", speed=0.03)
            loading_dots()
            break
        else:
            print("Invalid choice. Try again.")
            time.sleep(0.3)


def functions_menu(state):
    while True:
        lesson_header("FUNCTIONS")
        typewriter("Functions are reusable blocks of code. Define them using 'def' and call them by name.", speed=0.03)
        print()
        print("1. Simple Function Example")
        print("2. Function with Parameter and Return")
        print("3. Try Function Yourself")
        print("4. Scope & Local Variables (mini-explain)")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            separator()
            print("---- SIMPLE FUNCTION ----")
            print("def greet():")
            print("    print('Hello!')")
            print("greet()  # calling the function executes its code block and prints Hello!")
            print("output:")
            def greet():
                print("Hello!")
            greet()
            lesson_footer()

        elif choice == "2":
            separator()
            print("---- FUNCTION WITH PARAMETERS & RETURN ----")
            print("def add(a, b):")
            print("    return a + b")
            print("print(add(2, 3))  # prints 5")
            print("output:")
            def add(a, b):
                return a + b
            print(add(2, 3))
            lesson_footer()

        elif choice == "3":
            separator()
            typewriter("Try it: provide a name and we'll run a simulated greet function to show the output.", speed=0.03)
            separator()
            nm = input("Enter a name: ").strip() or "Friend"
            print("Function Output:")
            print(f"Hello, {nm}!  # printed by a function that received your input")
            press_to_continue()
            loading_dots()
            time.sleep(0.3)

        elif choice == "4":
            separator()
            typewriter("Variables defined inside functions are local to that function; they do not affect variables outside unless returned or declared global.", speed=0.03)
            separator()
            print()
            print("def my_func():")
            print("    x = 10  # local to my_func")
            print("x = 5")
            print("my_func()")
            print("print(x)  # prints 5 because the local x did not change the global x")
            print("output:")
            print(5)
            lesson_footer()

        elif choice == "5":
            typewriter("Going back to main menu...", speed=0.03)
            loading_dots()
            break
        else:
            print("Invalid choice. Try again.")
            time.sleep(0.3)


def arrays_menu(state):
    while True:
        lesson_header("ARRAYS / LISTS")
        typewriter("Lists (arrays) store ordered collections of items and are mutable.", speed=0.03)
        print()
        print("1. Create and Access a List")
        print("2. Append & Remove Items")
        print("3. Try Manage Your Own List")
        print("4. List Methods & Slicing")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            separator()
            print("---- CREATE & ACCESS ----")
            print("fruits = ['apple', 'banana', 'mango']")
            print("print(fruits[0])  # prints first item -> 'apple'")
            print("output:")
            fruits = ['apple', 'banana', 'mango']
            print(fruits[0])
            lesson_footer()

        elif choice == "2":
            separator()
            print("---- APPEND & REMOVE ----")
            print("numbers = [1, 2, 3]")
            print("numbers.append(4)   # now [1,2,3,4]")
            print("numbers.pop()       # removes and returns last item")
            print("output demonstration:")
            numbers = [1, 2, 3]
            numbers.append(4)
            print(numbers)
            numbers.pop()
            print("After pop:", numbers)
            lesson_footer()

        elif choice == "3":
            separator()
            typewriter("Interactive list: add items until you type 'done'. We'll show the evolving list each time.", speed=0.03)
            separator()
            user_list = []
            while True:
                item = input("Add an item (or type 'done' to finish): ").strip()
                if item.lower() == "done":
                    break
                user_list.append(item)
                print("Current list:", user_list)
            print("Final list:", user_list)
            press_to_continue()
            loading_dots()
            time.sleep(0.3)

        elif choice == "4":
            separator()
            typewriter("Common list operations: len(list), list[index], list[start:end], list.sort(), list.reverse()", speed=0.03)
            separator()
            print()
            print("example: members = ['a','b','c']")
            print("print(len(members))        # number of items")
            print("print(members[0:2])        # slice first two items")
            print("members.sort()             # sorts list in place")
            lesson_footer()

        elif choice == "5":
            typewriter("Going back to main menu...", speed=0.03)
            loading_dots()
            break
        else:
            print("Invalid choice. Try again.")
            time.sleep(0.3)


def dictionary_menu(state):
    while True:
        lesson_header("DICTIONARIES (KEY-VALUE PAIRS)")
        typewriter("Dictionaries store data as key-value pairs and are very useful for structured data.", speed=0.03)
        print()
        print("1. Create and Access a Dictionary")
        print("2. Update and Remove Items")
        print("3. Try Creating a Dictionary")
        print("4. Dictionary Methods (keys, values, items)")
        print("5. Back to Main Menu")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            separator()
            print("---- CREATE & ACCESS ----")
            print("person = {'name': 'Kyky', 'age': 18}")
            print("print(person['name'])  # access value by key")
            print("output (example):")
            person = {'name': state.get("name_example", "Kyky"), 'age': state.get("age_example", 18)}
            print(person['name'])
            lesson_footer()

        elif choice == "2":
            separator()
            print("---- UPDATE & REMOVE ----")
            print("person['age'] = 19    # updates the age value")
            print("del person['age']     # deletes the key 'age'")
            print("output demonstration:")
            person = {'name': 'Kyky', 'age': 18}
            person['age'] = 19
            print("After update:", person)
            del person['age']
            print("After deletion:", person)
            lesson_footer()

        elif choice == "3":
            separator()
            typewriter("Try it: enter keys and values to build a small dictionary interactively.", speed=0.03)
            separator()
            user_dict = {}
            while True:
                k = input("Enter key (or 'done' to finish): ").strip()
                if k.lower() == "done":
                    break
                v = input("Enter value: ").strip()
                user_dict[k] = v
                print("Current dictionary:", user_dict)
            print("Final dictionary:", user_dict)
            press_to_continue()
            loading_dots()
            time.sleep(0.3)

        elif choice == "4":
            separator()
            typewriter("Common dictionary methods: dict.keys(), dict.values(), dict.items()", speed=0.03)
            separator()
            print()
            example = {'a': 1, 'b': 2}
            print("example.keys() ->", list(example.keys()))
            print("example.values() ->", list(example.values()))
            print("example.items() ->", list(example.items()))
            lesson_footer()

        elif choice == "5":
            typewriter("Going back to main menu...", speed=0.03)
            loading_dots()
            break
        else:
            print("Invalid choice. Try again.")
            time.sleep(0.3)

# ---------------------------
# Extra utilities and mini-features
# ---------------------------

def quick_quiz(state):
    """A short quiz combining several modules to collect a small score."""
    lesson_header("QUICK QUIZ")
    typewriter("Answer these 5 quick questions. Each correct answer gives 1 point.", speed=0.02)
    score = 0

    q1 = input("1) Which function prints output in Python? ").strip().lower()
    if q1 in ("print", "print()"):
        score += 1
        print("Correct!")
    else:
        print("Answer: print()")

    q2 = input("2) What operator concatenates strings? (symbol or word) ").strip().lower()
    if q2 in ("+", "plus", "concatenate", "concat"):
        score += 1
        print("Correct!")
    else:
        print("Answer: + (plus)")

    q3 = input("3) True/False: '==' checks if two values are equal. ").strip().lower()
    if q3 and q3[0] == "t":
        score += 1
        print("Correct!")
    else:
        print("Answer: True")

    q4 = input("4) What keyword defines a function? ").strip().lower()
    if q4 == "def":
        score += 1
        print("Correct!")
    else:
        print("Answer: def")

    q5 = input("5) Which list method adds an item to the end? ").strip().lower()
    if q5 == "append":
        score += 1
        print("Correct!")
    else:
        print("Answer: append")

    print()
    print(f"Your quick quiz score: {score}/5")
    state["last_quiz_score"] = score
    save_progress(state)
    press_to_continue()
    loading_dots()
    time.sleep(0.3)


# ---------------------------
# Main Menu (single-file consolidated)
# ---------------------------

def main():
    state = load_progress()
    clear_screen()
    typewriter("Hello po, welcome to my Python Interactive Menu Program.", speed=0.03)
    name = input("What is your name --> ").strip() or "Student"
    state["user_name"] = name
    print()
    typewriter(f"Hello, {name}! Again, Welcome to my finals, hope you learn today here!", speed=0.04)
    # Save some defaults to state so examples show user's name
    state.setdefault("name_example", name)
    state.setdefault("age_example", 18)
    save_progress(state)
    time.sleep(0.6)
    start_program = input("Do you want to start? (Yes or No): ").strip()
    print()
    if start_program.lower() == "yes":
        loading_dots(3, 0.5)
        # Show main menu loop
        while True:
            clear_screen()
            banner("PYTHON LESSON MAIN MENU")
            print(f"User: {state.get('user_name', 'Student')}")
            print()
            print("1. Printing")
            print("2. Variables")
            print("3. Conditionals")
            print("4. Operators")
            print("5. Loops")
            print("6. Functions")
            print("7. Arrays / Lists")
            print("8. Dictionary")
            print("9. Quick Quiz")
            print("0. Exit")
            main_choice = input("Enter your choice: ").strip()
            print()
            loading_dots(3, 0.4)

            if main_choice == "1":
                printing_menu(state)
            elif main_choice == "2":
                variables_menu(state)
            elif main_choice == "3":
                conditionals_menu(state)
            elif main_choice == "4":
                operators_menu(state)
            elif main_choice == "5":
                loops_menu(state)
            elif main_choice == "6":
                functions_menu(state)
            elif main_choice == "7":
                arrays_menu(state)
            elif main_choice == "8":
                dictionary_menu(state)
            elif main_choice == "9":
                quick_quiz(state)
            elif main_choice == "0":
                typewriter(f"Goodbye, {state.get('user_name', name)}! Thanks for using the interactive lessons.", speed=0.03)
                save_progress(state)
                break
            else:
                print("Invalid choice. Try again.")
                time.sleep(0.6)

    else:
        typewriter("Okay, see you next time. Program ended.", speed=0.03)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting.")