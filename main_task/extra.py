# Extras:
# If the number is a multiple of 4, print out “divisible by 4”.
number = input("Insert your number: ")
number = int(number)
if number % 4 == 0:
    print(f"{number} is a multiple of 4")
else:
    print(f"{number} is not a multiple of 4")