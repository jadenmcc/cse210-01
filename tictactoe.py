# W02 Prove: Developer - Solo Code Submission
# by Jaden McCarrey

# Your program must also meet the following requirements.
# 1. The program must have a comment with assignment and author names.
# 2. The program must have at least one if/then block.
# 3. The program must have at least one while loop.
# 4. The program must have more than one function.
# 5. The program must have a function called main.

game_board = {
    "a1": 1,
    "a2": 2,
    "a3": 3,
    "b1": 4,
    "b2": 5,
    "b3": 6,
    "c1": 7,
    "c2": 8,
    "c3": 9
}

def main():
    print_board(game_board)
    print()

    game_status = get_game_status(game_board)

    turn = 1

    while game_status == "game on":
        play_round(game_board, turn)
        turn += 1
        print()
    
        print_board(game_board)
        print()

        game_status = get_game_status(game_board)

    print("Good game. Thanks for playing!")
    print()
    

def print_board(game_board):
    print(f'{game_board["a1"]} | {game_board["a2"]} | {game_board["a3"]}')
    print(f"-+-+-+-+-")
    print(f'{game_board["b1"]} | {game_board["b2"]} | {game_board["b3"]}')
    print(f"-+-+-+-+-")
    print(f'{game_board["c1"]} | {game_board["c2"]} | {game_board["c3"]}')


def play_round(game_board, turn):
    if (turn % 2) > 0:
        active_player = "x"
        other_player = "o"
    else:
        active_player = "o"
        other_player = "x"

    turn_status = ""

    while turn_status == "":
        player_choice = int(input(f"{active_player}'s turn to choose a square (1-9): "))

        if player_choice == 1:
            if game_board["a1"] != other_player and game_board["a1"] != active_player:
                game_board["a1"] = active_player
                turn_status = "over"
            else:
                print("That square is already taken. Choose another square.")
                print()
        elif player_choice == 2:
            if game_board["a2"] != other_player and game_board["a2"] != active_player:
                game_board["a2"] = active_player
                turn_status = "over"
            elif game_board["a2"] == other_player or active_player:
                print("That square is already taken. Choose another square.")
                print()
                player_choice = int(input(f"{active_player}'s turn to choose a square (1-9): "))
                print()
        elif player_choice == 3:
            if game_board["a3"] != other_player and game_board["a3"] != active_player:
                game_board["a3"] = active_player
                turn_status = "over"
            elif game_board["a3"] == other_player or active_player:
                print("That square is already taken. Choose another square.")
                print()
                player_choice = int(input(f"{active_player}'s turn to choose a square (1-9): "))
                print()
        elif player_choice == 4:
            if game_board["b1"] != other_player and game_board["b1"] != active_player:
                game_board["b1"] = active_player
                turn_status = "over"
            elif game_board["b1"] == other_player or active_player:
                print("That square is already taken. Choose another square.")
                print()
                player_choice = int(input(f"{active_player}'s turn to choose a square (1-9): "))
                print()
        elif player_choice == 5:
            if game_board["b2"] != other_player and game_board["b2"] != active_player:
                game_board["b2"] = active_player
                turn_status = "over"
            elif game_board["b2"] == other_player or active_player:
                print("That square is already taken. Choose another square.")
                print()
                player_choice = int(input(f"{active_player}'s turn to choose a square (1-9): "))
                print()
        elif player_choice == 6:
            if game_board["b3"] != other_player and game_board["b3"] != active_player:
                game_board["b3"] = active_player
                turn_status = "over"
            elif game_board["b3"] == other_player or active_player:
                print("That square is already taken. Choose another square.")
                print()
                player_choice = int(input(f"{active_player}'s turn to choose a square (1-9): "))
                print()
        elif player_choice == 7:
            if game_board["c1"] != other_player and game_board["c1"] != active_player:
                game_board["c1"] = active_player
                turn_status = "over"
            elif game_board["c1"] == other_player or active_player:
                print("That square is already taken. Choose another square.")
                print()
                player_choice = int(input(f"{active_player}'s turn to choose a square (1-9): "))
                print()
        elif player_choice == 8:
            if game_board["c2"] != other_player and game_board["c2"] != active_player:
                game_board["c2"] = active_player
                turn_status = "over"
            elif game_board["c2"] == other_player or active_player:
                print("That square is already taken. Choose another square.")
                print()
                player_choice = int(input(f"{active_player}'s turn to choose a square (1-9): "))
                print()
        elif player_choice == 9:
            if game_board["c3"] != other_player or game_board["c3"] != active_player:
                game_board["c3"] = active_player
                turn_status = "over"
            elif game_board["c3"] == other_player or active_player:
                print("That square is already taken. Choose another square.")
                print()
                player_choice = int(input(f"{active_player}'s turn to choose a square (1-9): "))
                print()
        else:
            print("Invalid choice. Please try again by selecting a number from 1-9 inclusive.")


def get_game_status(game_board):
    if (game_board["a1"] == "x" and game_board["a2"] == "x" and game_board["a3"] == "x") or (game_board["a1"] == "o" and game_board["a2"] == "o" and game_board["a3"] == "o"):
        game_status = "game over"
    elif (game_board["b1"] == "x" and game_board["b2"] == "x" and game_board["b3"] == "x") or (game_board["b1"] == "o" and game_board["b2"] == "o" and game_board["b3"] == "o"):
        game_status = "game over"
    elif (game_board["c1"] == "x" and game_board["c2"] == "x" and game_board["c3"] == "x") or (game_board["c1"] == "o" and game_board["c2"] == "o" and game_board["c3"] == "o"):
        game_status = "game over"
    elif (game_board["a1"] == "x" and game_board["b1"] == "x" and game_board["c1"] == "x") or (game_board["a1"] == "o" and game_board["b1"] == "o" and game_board["c1"] == "o"):
        game_status = "game over"
    elif (game_board["a2"] == "x" and game_board["b2"] == "x" and game_board["c2"] == "x") or (game_board["a2"] == "o" and game_board["b2"] == "o" and game_board["c2"] == "o"):
        game_status = "game over"
    elif (game_board["a3"] == "x" and game_board["b3"] == "x" and game_board["c3"] == "x") or (game_board["a3"] == "o" and game_board["b3"] == "o" and game_board["c3"] == "o"):
        game_status = "game over"
    elif (game_board["a1"] == "x" and game_board["b2"] == "x" and game_board["c3"] == "x") or (game_board["a1"] == "o" and game_board["b2"] == "o" and game_board["c3"] == "o"):
        game_status = "game over"
    elif (game_board["a3"] == "x" and game_board["b2"] == "x" and game_board["c1"] == "x") or (game_board["a3"] == "o" and game_board["b2"] == "o" and game_board["c1"] == "o"):
        game_status = "game over"
    elif game_board["a1"] != 1 and game_board["a2"] != 2 and game_board["a3"] != 3 and game_board["b1"] != 4 and game_board["b2"] != 5 and game_board["b3"] != 6 and game_board["c1"] != 7 and game_board["c2"] != 8 and game_board["c3"] != 9:
        game_status = "game over"
    else:
        game_status = "game on"

    return game_status

if __name__ == "__main__":
    main()