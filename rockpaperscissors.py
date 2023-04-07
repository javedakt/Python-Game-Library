import random
import datetime


def rps_game():

    # Making log file to store wins, losses, and draws along with what time they occurred. Try/except incase the log already exists

    try:
        rps_game_log = open("RPS_Log.txt", "x")
    except:
        pass

    # Greeting / introduction

    print("""Welcome to Rock, Paper, Scissors!

The winner of this game will be the best out of 5 rounds.""")
    print("----------------------------------------")

    # Giving the user the choice to play between a friend or the computer, kept inside a while loop incase they don't enter "F" or "C"

    while True:
        fr_or_co = str(input(
            "Would you like to play against a friend (F) or the computer? (C)\n").capitalize())
        if fr_or_co == "F":
            break
        elif fr_or_co == "C":
            break
        else:
            print("Please enter F or C!")

    # A list created for computer to randomly pick choices from. Originally was only 3 items but computer kept making same choice, so added more of the same for greater variety

    comp_choices = ["R", "P", "S", "R", "P", "S", "R", "P", "S"]

    # Making placeholder variables for the number of rounds and player scores

    rounds = 0
    player1_score = 0
    player2_score = 0

    while True:

        # Everytime the while loop is rerun, 'rounds' gets added to. Once it reaches 5, the while loop exits

        rounds += 1
        print("----------------------------------------")
        player1 = input("PLAYER 1, please enter R, P, or S: ").capitalize()

        # Input for both players, along with a random computer-generated choice for player 2 if the user selected they want to play against the computer earlier

        if fr_or_co == "F":
            player2 = input(
                "PLAYER 2, please enter R, P, or S: ").capitalize()
            print("")
        else:
            player2 = random.choice(comp_choices)
            print(f'Computer chose "{player2}"!\n')

        # Logic for determining the winner, every possible outcome is accounted for

        if player1 == player2:
            print(
                f"Both players picked the same item. No one wins round {rounds}.")

        elif player1 == "R" and player2 == "S":
            print(f"Rock beats Scissors, PLAYER 1 wins round {rounds}.")
            player1_score += 1
        elif player2 == "R" and player1 == "S":
            print(f"Rock beats Scissors, PLAYER 2 wins round {rounds}.")
            player2_score += 1

        elif player1 == "P" and player2 == "R":
            print(f"Paper beats Rock, PLAYER 1 wins round {rounds}.")
            player1_score += 1
        elif player2 == "P" and player1 == "R":
            print(f"Paper beats Rock, PLAYER 2 wins round {rounds}.")
            player2_score += 1

        elif player1 == "S" and player2 == "P":
            print(f"Scissors beats Paper, PLAYER 1 wins round {rounds}.")
            player1_score += 1
        elif player2 == "S" and player1 == "P":
            print(f"Scissors beats Paper, PLAYER 2 wins round {rounds}.")
            player2_score += 1

        # A display of each player's score displayed every round

        print(f""" _______________________
| PLAYER 1's score is {player1_score} |
| PLAYER 2'S score is {player2_score} |
-------------------------""")

        # If the number of rounds reaches 5, the results are written to the log file created in the beginning, and while loop exits

        if rounds == 5:
            if player1_score == player2_score:
                print("Both players tied, no one wins.")
                rps_game_log = open("RPS_Log.txt", "a")
                rps_game_log.write(
                    f"{datetime.datetime.now()} : Both players tied in RPS, no one wins\n")
                rps_game_log.close()
            elif player1_score > player2_score:
                print("PLAYER 1 wins the game!")
                rps_game_log = open("RPS_Log.txt", "a")
                rps_game_log.write(
                    f"{datetime.datetime.now()} : PLAYER 1 is victorious over PLAYER 2 in RPS\n")
                rps_game_log.close()
            else:
                print("PLAYER 2 wins the game!")
                rps_game_log = open("RPS_Log.txt", "a")
                rps_game_log.write(
                    f"{datetime.datetime.now()} : PLAYER 2 is victorious over PLAYER 1 in RPS\n")
                rps_game_log.close()
            break

    # Another while loop incase the user doesn't input Y or N

    while True:
        play_again = input(
            "Do you want to play again? Y or N\n").capitalize()
        if play_again == "N":
            print("Thank you for playing!")
            return
        elif play_again == "Y":
            rps_game()
        else:
            print("Please enter Y or N!")
