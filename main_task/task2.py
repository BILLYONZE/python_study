# TASK 2: Using Python or PHP or Java or Ruby or JavaScript
# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
number = input("Type your number: ")
number = int(number)
if number%2 == 0:
    print(f"{number} is an Even Number")
else:
    print(f"{number} is an Odd Number")