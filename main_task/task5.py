# TASK 5: Using Python or PHP or Java or Ruby or JavaScript
# Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores them in three variables. Return the largest of the three. Do this without using the the inbuilt max () function!
# The goal of this exercise is to think about some internals that programs normally take care of for us. 
input1 = input("number 1: ")
x= int(input1)
input2 = input("number 2: ")
y= int(input2)
input3 = input("number 3: ")
z= int(input3)
if x > y and x > z:
    print(f"{x} is the Greatest number")
elif y > x and y > z :
    print(f"{y}is the Greatest number")
else:
    print(f"{z} is the Greatest number")