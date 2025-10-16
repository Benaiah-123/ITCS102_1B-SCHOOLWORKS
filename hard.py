user_loan = eval(input("Enter your loan amount: "))
user_duration = eval(input("Enter your loan duration (in years): "))

months = user_duration * 12
principal = user_loan / months
balance = user_loan

print("|Month\t|Principal\t|Interest\t|Balance\t   |Monthly Payment")
for duration in range(1, months + 1, 1):
    balance -= principal
    interest = balance * 0.03
    monthly = round((principal + interest), 2)
    print(duration,"\t|", round(principal, 2), "         |", round(interest, 2), "         |", round(balance, 3), "         |", monthly)