def area_of_triangle():
    height = 20
    base = 10
    area = (base * height)/2
    print(area)
area_of_triangle()

# a function that checks if a number is even or odd
def even_or_odd():
    x=21
    if x %2 ==0:
        print(f"{x} is an even number")
    else:
        print(f"{x} is an odd number")
even_or_odd()

# a function that calculates the area of a rectangle.
def area_of_rectangle():
    length =20
    width = 0.4
    area = length * width
    print(area)
area_of_rectangle()

# a function that displays the largest number among three numbers.
def largest_number():
    x =2
    y = 3
    z = 4
    if x>y and x>z:
        print(f"{x} is the Largest number")
    elif y>x and y> z:
        print(f"{y} is the Largest number")
    else:
        print(f"{z} is the Largest number")
largest_number()
