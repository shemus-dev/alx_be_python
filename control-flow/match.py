import random

# secret_number =  random.randint(1,20)
# guess = int(input("guess a number"))

# match guess:
#     case _ if guess == secret_number:
#           print("Congratulations you guessed it!")
#     case _ if guess >= secret_number:
#           print("Oops, your guess is a bit high. Try again")

#     case _ if guess <= secret_number:
#           print("Nope, your guess is a bit low. Give it another shot!")

#     case __ :
#           print("game over")


while True:  # Loop to allow replaying the game
    secret_number = random.randint(1, 20)
    guess_count = 0

    print("I'm thinking of a number between 1 and 20. Can you guess it?")

    while True:  # Loop for guessing the secret number
        guess = int(input("Guess a number: "))
        guess_count += 1  # Count the guess

        match guess:
            case _ if guess == secret_number:
                print(f"Congratulations, you guessed it in {guess_count} guesses!")
                break  # Exit guessing loop; user won
            case _ if guess > secret_number:
                print("Oops, your guess is a bit high. Try again!")
            case _ if guess < secret_number:
                print("Nope, your guess is a bit low. Give it another shot!")

    play_again = input("Play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break  # Exit the main loop; end the game

 

# day = input("Enter a day of the week").lower()

# match day:
#     case "monday":
#         print("its monday")
#     case "tuesday | wednesday":
#          print("its today")
#     case _:
#         print("Entered an invalid day")
     