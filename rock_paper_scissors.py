import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0

print("🎮 Rock Paper Scissors Championship")
print("First to win the most rounds out of 5 becomes the champion!\n")

for round_num in range(1, 6):
    print(f"\n--- Round {round_num} ---")

    player = input("Choose rock, paper, or scissors: ").lower()

    while player not in choices:
        player = input("Invalid choice! Choose rock, paper, or scissors: ").lower()

    computer = random.choice(choices)

    print(f"Computer chose: {computer}")

    if player == computer:
        print("🤝 Draw!")

    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        print("🎉 You win this round!")
        player_score += 1

    else:
        print("😢 Computer wins this round!")
        computer_score += 1

    print(f"Score: You {player_score} - {computer_score} Computer")

print("\n🏆 FINAL RESULTS 🏆")
print(f"You: {player_score}")
print(f"Computer: {computer_score}")

if player_score > computer_score:
    print("🎉 Congratulations! You are the CHAMPION!")

elif computer_score > player_score:
    print("😢 Computer is the CHAMPION!")

else:
    print("🤝 The championship ended in a DRAW!")
