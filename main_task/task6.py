# TASK 6:Using Python or PHP or Java or Ruby or JavaScript
# Write a program that lets the user input a password.
#  Give them only 4 attempts to check the passwords entered against “admin@123”.
#  If the password is correct access is granted. After you show them a message , the account is blocked.
pas = "admin@123"
att = 4
for i in range(1,att + 1):
    pin = input("Kindly insert your pin: ")
    if pin == pas:
        print("access granted")
        break
    else:
         attempts_left = att - i
         print("Wrong pin")
         if attempts_left > 0:
             print(f"You are left with {attempts_left} remaining")
         else:
             print("Your account is blocked")
         