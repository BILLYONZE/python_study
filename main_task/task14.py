# TASK 14: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that takes input of 2 values and adds them.
#  The program should only accept numbers and floats only or otherwise display an error “invalid character entered”
#  and take the user to re-enter the inputs .
while True:
    try:
        num1 = input("Enter a number: ")
        num1 = float(num1)
        num2 = input("Enter another number: ")
        num2 = float(num2) 
        valid = num1 + num2
        # num1 == float(num1) and num2 == float(num2)
        # valid = num1 + num2
        print(valid)
        break
    except:
        valid = "Invalid character Entered.Try Again"
        print(valid)
