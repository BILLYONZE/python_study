# TASK 2: Using Python or PHP or Java or Ruby or JavaScript
# Prompt the user for a number either on a form input or the terminal. Depending on whether the number is even or odd, display  either “odd” or “even” to the user.
#  Hint: how does an even / odd number react differently when divided by 2?
def even_or_odd(number):
    if number%2 == 0:
        answer = f"{number} is an Even number"
    else:
        answer = f"{number} is an Odd number"
    return answer
number = input("Type your number: ")
number = int(number)
num = even_or_odd(number)
print(num)

