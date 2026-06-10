import random

categories = {
    "Technology": [
        "python",
        "github",
        "computer",
        "developer",
        "keyboard"
    ],
    "Animals": [
        "elephant",
        "giraffe",
        "penguin",
        "tiger",
        "dolphin"
    ],
    "Countries": [
        "india",
        "japan",
        "france",
        "canada",
        "brazil"
    ]
}

score = 0
best_streak = 0
streak = 0

print("🎮 ULTIMATE HANGMAN")

while True:

    category = random.choice(list(categories.keys()))
    word = random.choice(categories[category])

    guessed_letters = []
    lives = 6

    print("\n" + "=" * 40)
    print(f"📚 Category: {category}")
    print("=" * 40)

    while lives > 0:

        display = ""

        for letter in word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "

        print("\nWord:", display)

        if "_" not in display:
            print("🎉 You guessed the word!")

            score += 1
            streak += 1

            if streak > best_streak:
                best_streak = streak

            print(f"🏆 Score: {score}")
            print(f"🔥 Streak: {streak}")
            break

        print(f"❤️ Lives: {lives}")

        guess = input("Guess a letter (or type 'hint'): ").lower()

        if guess == "hint":
            hidden_letters = [
                letter for letter in word
                if letter not in guessed_letters
            ]

            if hidden_letters:
                hint_letter = random.choice(hidden_letters)
                guessed_letters.append(hint_letter)
                lives -= 1
                print(f"💡 Hint: The word contains '{hint_letter}'")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            lives -= 1
            print("❌ Wrong guess!")

    else:
        print(f"\n💀 Game Over!")
        print(f"The word was: {word}")

        streak = 0

    print("\n📊 Current Statistics")
    print(f"🏆 Score: {score}")
    print(f"🔥 Best Streak: {best_streak}")

    again = input("\nPlay another round? (y/n): ").lower()

    if again != "y":
        break

print("\n🏁 Final Statistics")
print(f"🏆 Total Wins: {score}")
print(f"🔥 Best Streak: {best_streak}")
print("Thanks for playing!")
