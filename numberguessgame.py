import random
import datetime


def guessing_game():

    # Making log file to store wins and losses along with what time they occurred
    try:
        guessing_game_log = open("NumberGuess_Log.txt", "x")
    except:
        pass

    while True:

        # Prompting user to choose a range of numbers for the computer to choose from

        print("""Welcome to the guessing game! Try to guess what number I'm thinking of!
-----------------------------------------------------------------------
To play, enter a MIN and MAX number below""")
        try:
            while True:
                user_min = int(input("MIN: "))
                user_max = int(input("MAX: "))
                if (user_min or user_max) < 0:
                    print("Please only enter positive numbers!")
                else:
                    break
        except:
            print("You did not enter a number!")
            guessing_game()

        # Using the 'random' module to choose a random integer based off the user's input
        computer_choice = random.randint(user_min, user_max)
        print(f"I have chosen a number between {user_min} and {user_max}.")

        # Storing the variable for the amount of guesses the user has, along with a list of random insults for them losing
        no_guesses = 5

        # A list of random insults incase the user runs out of guesses and loses
        insults = [
            "You suck at this!",
            "A baby could do better!",
            "I expected too much from a human.",
            "Did it hurt... when you were dropped on the head as a baby?"
        ]

        while True:
            try:
                user_guess = int(input(
                    f"What number am I thinking of? You have {no_guesses} guess(es) remaining.\n"))

        # If the user guesses right, the program ends
                if user_guess == computer_choice:
                    print("Wow! You guessed right, congrats!")
                    guessing_game_log = open("NumberGuess_Log.txt", "a")
                    guessing_game_log.write(
                        f"{datetime.datetime.now()} : USER beat CPU at guessing game\n")
                    guessing_game_log.close()
                    break

        # Otherwise if you're wrong, it continues until you run out of guesses. Then it insults you.
                elif user_guess != computer_choice:

                    # Subtracting a guess everyime the loop is run again
                    no_guesses -= 1

                    # Subtracting the computer's number from the user's guess to determine which hint to output
                    hot_cold = user_guess - computer_choice

                    # When the user runs out of guesses, a random insult is chosen from the list (line 35) and reveals the number the computer randomly chose
                    if no_guesses == 0:
                        print(
                            f"{random.choice(insults)} My number was {computer_choice}. You lose!")

                        # Simultaneously, the result is written to a log file created earlier
                        guessing_game_log = open("NumberGuess_Log.txt", "a")
                        guessing_game_log.write(
                            f"{datetime.datetime.now()} : USER lost to CPU at guessing game\n")
                        guessing_game_log.close()
                        break

                    # Logic for determining whether or not the user should guess higher/lower. If (user - computer) = negative, go higher. Else, positive
                    elif hot_cold < 0:
                        print("Wrong! Go higher!")
                        print(
                            "-----------------------------------------------------------")
                    else:
                        print("Wrong! Go lower!")
                        print(
                            "-----------------------------------------------------------")
            except:
                print("You did not enter a number!")

        # Asking user if they want to play again. If Y, the function restarts. Else it ends here.
        print("-----------------------------------------------------------")
        retry = input("Do you want to play again? Y or N\n").capitalize()

        if retry == "Y":
            guessing_game()
        elif retry == "N":
            print("Thank you for playing!")
        break
