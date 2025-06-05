pin = "Billyonze"
attempts = 5
for b in range(1,attempts+1):
    guess = input("Bitte Konnen Sie das Pin eingeben: ")
    if guess == pin:
        print("Das pin is Richtig")
        break
    else:
        attempts_remaining = attempts - b
        print(f". Das PIN ist falsch.Sie haben nur {attempts_remaining} chancen" )
        if attempts_remaining == 0:
            print("Es tut mir wirklich leid aber dieses Handy ist nicht seines")