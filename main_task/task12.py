# TASK 12: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prints the largest of 4 inputs taken as input from a user.
def largest_input(num1,num2,num3,num4):
    if num1>num2 and num1>num3 and num1>num4:
        solu =f"{num1} is the largest number"  
    elif num2>num2 and num2>num3 and num2 > num4:
        solu =f"{num2} is the greatest number"
    elif num3> num1 and num3>num2 and num3>num4:
        solu =f"{num3} is the greatest number"
    else:
        solu =f"{num4} is the greatest number"
    return solu
num1=input("Enter 4 numbers at a time: ")
num1 = int(num1)
num2=input()
num2=int(num2)
num3=input()
num3=int(num3)
num4=input()
num4=int(num4)
n = largest_input(num1,num2,num3,num4)
print (n)
