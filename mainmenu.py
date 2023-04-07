import numberguessgame
import rockpaperscissors


def game_library():

    # Introduction and visual menu

    print("Hello! Welcome to my Python Game Library!")
    print("-----------------------------------------")
    print("""Please select a game from the list below:
1. Number Guess Game
2. Rock Paper Scissors""")
    print("-----------------------------------------")
    print("9. Exit\n")

    # Try/Except incase the user input is not a number
    try:
        # While loop incase the user inputted number is not one of the available choices
        while True:
            game_select = int(input("Enter the corresponding number: "))
            print("-----------------------------------------")
            if game_select == 1:
                break
            elif game_select == 2:
                break
            elif game_select == 9:
                break
            else:
                print("Please enter 1, 2, or 9!")
    except:
        print("Please enter a number!")
        print("----------------------")
        game_library()

    # Depending on what the user selection is, launch the corresponding game, then relaunch this menu once the user exits the game

    if game_select == 1:
        numberguessgame.guessing_game()
        game_library()

    elif game_select == 2:
        rockpaperscissors.rps_game()
        game_library()

    # A way to exit this menu altogether

    elif game_select == 9:
        return


game_library()
