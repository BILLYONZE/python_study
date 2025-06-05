# TASK 13: Using Python or PHP or Java or Ruby or JavaScript or C# or Go
# Write a program that takes the email and password as input from a user and checks if they are equal to “admin@mail.com”
#  and password is “Admin@123” , if so then print  “Login is Successful” and if not print “Invalid username or password”.
#  ONLY accept 3 tries after which it notifies you that you have been blocked.
email = "admin@mail.com"
password = "Admin@123"
tries = 3
for i in range(1,tries +1):
    ema= input("Enter your Email address: ")
    pin = input("Enter your Password: ")
    if ema == email and pin == password:
        print("Login is Successful")
        break
    else:
        print("Invalid username or password")
        rem_att = tries - i
        if i > 0:
            print(f"Try again. You have {rem_att} attempts remaining")
        else:
                print("Incorrect Password")


