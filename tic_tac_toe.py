import random


def print_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def check_winner(board, player):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combo in winning_combinations:
        if all(board[pos] == player for pos in combo):
            return True

    return False


print("=" * 50)
print("🏆 TIC TAC TOE CHAMPIONSHIP")
print("=" * 50)

print("\nChoose Game Mode:")
print("1. Play vs Computer 🤖")
print("2. Play vs Friend 👥")

game_mode = input("Enter 1 or 2: ")

player_x_score = 0
player_o_score = 0
round_number = 1

while player_x_score < 2 and player_o_score < 2:

    print("\n" + "=" * 50)
    print(f"🎮 ROUND {round_number}")
    print("=" * 50)

    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    current_player = "X"

    while True:

        print_board(board)

        try:

            # Computer Turn
            if game_mode == "1" and current_player == "O":

                available_moves = []

                for i in range(9):
                    if board[i] not in ["X", "O"]:
                        available_moves.append(i)

                move = random.choice(available_moves)

                print(f"🤖 Computer chooses position {move + 1}")

            # Human Turn
            else:

                move = int(
                    input(
                        f"Player {current_player}, choose a position (1-9): "
                    )
                ) - 1

                if move < 0 or move > 8:
                    print("❌ Choose a number from 1 to 9.")
                    continue

                if board[move] in ["X", "O"]:
                    print("❌ That position is already taken.")
                    continue

            board[move] = current_player

            if check_winner(board, current_player):

                print_board(board)

                if game_mode == "1" and current_player == "O":
                    print("🤖 Computer wins this round!")
                else:
                    print(f"🎉 Player {current_player} wins this round!")

                if current_player == "X":
                    player_x_score += 1
                else:
                    player_o_score += 1

                break

            if all(space in ["X", "O"] for space in board):
                print_board(board)
                print("🤝 Round Draw!")
                break

            current_player = "O" if current_player == "X" else "X"

        except ValueError:
            print("❌ Please enter a valid number.")

    print("\n📊 CHAMPIONSHIP SCORE")

    if game_mode == "1":
        print(f"👤 Player: {player_x_score}")
        print(f"🤖 Computer: {player_o_score}")
    else:
        print(f"Player X: {player_x_score}")
        print(f"Player O: {player_o_score}")

    round_number += 1

print("\n" + "=" * 50)
print("🏆 CHAMPIONSHIP OVER")
print("=" * 50)

if game_mode == "1":

    if player_x_score > player_o_score:
        print("🥇 YOU ARE THE CHAMPION!")
    else:
        print("🤖 COMPUTER IS THE CHAMPION!")

else:

    if player_x_score > player_o_score:
        print("🥇 PLAYER X IS THE CHAMPION!")
    else:
        print("🥇 PLAYER O IS THE CHAMPION!")

print("\n🎉 Thanks for playing!")
