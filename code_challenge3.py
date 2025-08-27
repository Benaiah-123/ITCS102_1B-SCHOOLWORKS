name = input("enter your name here-->")
fare = float(input("enter your fare fee here-->"))
student = input("wait, are you student ? (yes/no)")

if student == "yes":
    discount = fare * 0.20
    new_fare = fare - discount
    print("welcome", name)
    print("your fare is", fare)
    print("the discounted fare for you is", new_fare)
else:
    print("welcome", name)
    print("Sorry, you are not eligable for discount")
    print("your fare is still", fare)
       
