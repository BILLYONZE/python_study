def area_of_triangle(base , height):
    area = (base * height)/2
    return area
p = area_of_triangle(10,30)
print (p)
area_of_triangle(4,5)

# a function that checks if a number is even or odd
def even_or_odd(num1):
    if num1 %2 ==0:
        print(f"{num1} is an even number")
    else:
        print(f"{num1} is an odd number")
even_or_odd(22)
even_or_odd(21)
even_or_odd(0)

# a function that calculates the area of a rectangle.
def area_of_rectangle(length,width):
    area = length * width
    print(area)
area_of_rectangle(99,17)
area_of_rectangle(66,5)

# a function that displanum2s the largest number among three numbers.
def largest_number(num1,num2,num3):
    if num1>num2 and num1>num3:
        print(f"{num1} is the Largest number")
    elif num2>num1 and num2> num3:
        print(f"{num2} is the Largest number")
    else:
        print(f"{num3} is the Largest number")
num1 = int(input(f"num1: "))
num2 = int(input(f"num2: "))
num3 = int(input(f"num3: "))

largest_number(num1,num2,num3)
