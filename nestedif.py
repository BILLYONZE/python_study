# Write a program that:
# = > Takes the user's credit score and annual income as input.
# =>If the credit score is above 700, check if the income is above 50,000:
# =>If both conditions are met, print "Loan approved."
# =>If only the credit score is high, print "Income requirement not met."
# =>If the credit score is below 700, print "Credit score too low."
credit_score =input("Enter your credit score: ")
credit_score = int(credit_score)
if credit_score >700:
    annual_income = input("Enter your annual income: ")
    annual_income = int(annual_income)
    if annual_income > 50000:
        print("Loan approved.")
    else:
        print("Income requirement not met.")
else:
    print("Credit score too low.")
# write a program that takes users age as input
# if the age is 18 and above ,check if they have  drivers license if they do we print you are eligible to drive
# if they dont have a drivers license print you are not eligible to drive
# otherwise you are too young to drive
age = input("Enter your age: ")
age = int(age)
if age >= 18:
    license = input("Do you have a driver's license? (yes/no): ").casefold()
    if license == "yes":
        print("You are eligible to drive.")
    else:
        print("You are not eligible to drive.")
else:
    print("You are too young to drive.")