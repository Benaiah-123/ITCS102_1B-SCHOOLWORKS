import os

print("STUDENT INFORMATION SYSTEM")
print("===============================")

#empty dictionary
student_record = {}

while True:
    #os.system('cls')
    print("SELECT FROM THE FOLLOWING OPTIONS")
    print("A- Add student record")
    print("B- Print all student record")
    print("C- Search student record")
    print("D- Delete student record")
    print("E- Edit student record")
    print("F- Export student record")
    print("G- Exit System")
    
    choice =input("Select from the options above -->  ").lower()

    if choice == 'a':
        os.system ('cls')
        print("\n ***ADDING STUDENT RECORD***")

        id_no=input("please enter your student id number --> ")

        firstname= input("enter your first name here--> ").upper()
        lastname= input("enter your last name here--> ").upper()
        age= eval(input("enter your age here--> "))
        section= input("enter your section in here--> ").upper()
        course= input("enter your program here--> ").upper()

        student_record[id_no]=[firstname,lastname,age,section,course]
        print("Student record data saved successfully.")

        



        
        continue
    elif choice == 'b':
        os.system('cls')
        print("PRINTING STUDENT RECORD")
        #print(student record) simple approach

        for i,j in student_record.items(): #key - values
            print(f"student id-{i}, Information - {j}")
        continue
    elif choice == 'c':
        pass
        continue
    elif choice == 'd':
        pass
        continue
    elif choice == 'e':
        pass
        continue
    elif choice == 'f':
        pass
        continue
    elif choice == 'g':
        print("The system stop")
        break

    else:
        print("its not on the option, do it again")
        break

