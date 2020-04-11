import random
test = True
user_guess = input("Guess a random number between 1-9: ")
random_number = random.randint(1, 9)

while test:

    try:
        user_guess = input("Guess a random number between 1-10: ")
        if int(user_guess) > 0 and int(user_guess) < 11:
            if int(user_guess) == random_number:
                print("Well Guessed!")
                break
        else:
            print("Please enter an integer between 1 to 9")
    except ValueError:
        print("You didnt enter a number, you probably entered a lwtter or a symbol ")
        continue