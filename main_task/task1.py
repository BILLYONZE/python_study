# TASK 1: Using Python or PHP or Java or Ruby or JavaScript
# Write a program that prompts the user to enter the base and height of a triangle and returns its area.
print("We are finding the area of Triangle A")
def area_of_Triangle(height,base):
    area = base * height * 0.5
    return area
height = float(input("Height: "))
base = float(input("Base: "))
a = area_of_Triangle(height,base)
print(a)
area_of_Triangle(10,40)