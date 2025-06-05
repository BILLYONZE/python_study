number = 2
attempts = 3
for i in range(1,attempts+1):
    guess = input("Guess the number: ")
    guess = int(guess)
    if guess == number:
        print("YAY!.You guessed the correct number")
        break
    else:
        remaining_attempts=attempts - i
        if remaining_attempts>0:
            print(f"You have {remaining_attempts} remaining")
        else:
            print("You have run out of attempts")
    