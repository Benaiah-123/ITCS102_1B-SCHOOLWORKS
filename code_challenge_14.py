import os
import json

os.system('cls')
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
        #storing data into a dictionary - student_record
        course= input("enter your program here--> ").upper()

        student_record[id_no]=[firstname,lastname,age,section,course]
       #go back to original menu
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
        os.system('cls')
        print('Search student record')

        search_id= input("Input student id for search -> ").lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print(" ====================== ")
                print(f"\n\nRecord Student Id for search{search_id}")
                #to print the record for the search id
                for i in student_record[search_id]:
                    print(f" --- {i}")

                print(" ====================== ")
            else:
                print("No Record Found")
            break   
        continue
    elif choice == 'd':
        os.system('cls')
        print('Search student record')

        search_id= input("Input student id for search -> ").lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print(" ====================== ")
                print(f"\n\nRecord Student Id for search{search_id}")
                #to print the record for the search id
                for i in student_record[search_id]:
                    print(f" --- {i}")

                print(" ====================== ")
                #.pop()to delete an item
                student_record.pop(search_id)
                print("\n Record Deleted")
            else:
                print("DATA UPDATED!!")
            break
        continue
    elif choice == 'e':
        os.system('cls')

        print("Edit/Modify Student Record")

        search_id=input("Input student id for search --> ").lower()

        for each_id in student_record.keys():
            if search_id in student_record.keys():
                print(" =======================")
                print(f"\n Record Found for Id{search_id}")
                #to print the record for the saarched id
                for i in student_record[search_id]:
                    print(f" ---{i}")
                print( " ======================")
                #new sets of value for the search ID    
            firstname= input("enter your first name here--> ").upper()
            lastname= input("enter your last name here--> ").upper()    
            age= eval(input("enter your age here--> ")) 
            section= input("enter your section in here--> ").upper()
            course= input("enter your program here--> ").upper()
            student_record[search_id][0]= firstname
            student_record[search_id][1]= lastname
            student_record[search_id][2]= age
            student_record[search_id][3]= course
            student_record[search_id][4]= section

            print("data updated")
        else:
            print("No Record Found")
        break
    elif choice == 'f':
        os.system('cls')
        print("Export Student Data")
        #json javascript object notation

        with open('student_record.json', 'w')as new_file:
            json.dump(student_record,new_file, indent=4)
        
        print("\n\n Data Exported to json")

        continue
    elif choice == 'g':
        print("system exit")
        break

    else:
        print("its not on the option, do it again")
        continue

