
# TASK 9: Using Python or PHP or Java or Ruby or JavaScript
# Write a program called stars. It should prompt the user for a number, and it should print the number of stars till the number entered.
# Example If rows is 5, it should print the following:
# *
# **
# ***
# ****
# *****.....
num = input("Enter Number: ")
num = int(num)
for i in range(1,num+1):
    i = i * "*"
    print(i)
