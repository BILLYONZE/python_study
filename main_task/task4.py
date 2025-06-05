# TASK 4: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.
# email = input("Insert your email address: ")
# email = str(email)
email = input("Insert your email address: ")
if "@" and "." in email:
    print(" Welcome home Billjoy")
else:
    print("Email inserted Incorrectly")