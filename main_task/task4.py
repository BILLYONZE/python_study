# TASK 4: Using Python or PHP or Java or Ruby or JavaScript
# Write a program which accepts email as form input or from terminal. Validate the email by checking if it's a valid email. 
# Hint: Check if it contains an “@” symbol and “.” symbol.
# email = input("Insert your email address: ")
# email = str(email)
def email_address(email):
    if "@" and "." in email:
        access = " Welcome home Billjoy"
    else:
        access ="Email inserted Incorrectly"
    return access
email = input("Insert your email address: ")
em = email_address(email)
print(em)
