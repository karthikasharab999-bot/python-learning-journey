import random

questions = [
    # Geography
    ("What is the capital of India?", "delhi", "Geography"),
    ("What is the capital of Japan?", "tokyo", "Geography"),
    ("Which is the largest ocean?", "pacific", "Geography"),
    ("Which country has the Eiffel Tower?", "france", "Geography"),
    ("What is the capital of Australia?", "canberra", "Geography"),

    # Science
    ("Which planet is known as the Red Planet?", "mars", "Science"),
    ("Which gas do plants absorb?", "carbon dioxide", "Science"),
    ("What is H2O commonly called?", "water", "Science"),
    ("What force keeps us on the ground?", "gravity", "Science"),
    ("What is the center of our solar system?", "sun", "Science"),

    # Math
    ("What is 12 x 12?", "144", "Math"),
    ("What is the square root of 64?", "8", "Math"),
    ("What is 25 + 17?", "42", "Math"),
    ("What is 100 divided by 4?", "25", "Math"),
    ("What is 15 x 3?", "45", "Math"),

    # Python
    ("Which programming language are we learning?", "python", "Python"),
    ("What function displays text?", "print", "Python"),
    ("What function gets user input from the keyboard?", "input", "Python"),
    ("What keyword creates a loop: for or repeat?", "for", "Python"),
    ("Which module generates random numbers?", "random", "Python"),

    # General Knowledge
    ("Who wrote Romeo and Juliet?", "shakespeare", "GK"),
    ("How many continents are there?", "7", "GK"),
    ("Which animal is called the King of the Jungle?", "lion", "GK"),
    ("How many days are there in a week?", "7", "GK"),
    ("What color do you get by mixing red and blue?", "purple", "GK"),

    ("What is the largest mammal?", "blue whale", "GK"),
    ("Which bird cannot fly?", "ostrich", "GK"),
    ("What is the national bird of India?", "peacock", "GK"),
    ("Which month comes after June?", "july", "GK"),
    ("How many hours are there in a day?", "24", "GK")
]

random.shuffle(questions)

score = 0
answered = 0
streak = 0
best_streak = 0

QUESTIONS_PER_ROUND = 8

print("=" * 50)
print("🧠 ULTIMATE QUIZ CHALLENGE")
print("=" * 50)
print("Type 'quit' anytime to finish.\n")

for i, (question, answer, category) in enumerate(questions):

    if i % QUESTIONS_PER_ROUND == 0:
        round_num = (i // QUESTIONS_PER_ROUND) + 1
        print("\n" + "=" * 50)
        print(f"🎮 ROUND {round_num}")
        print("=" * 50)

    print(f"\n📚 Category: {category}")

    user_answer = input(question + "\n> ").lower().strip()

    if user_answer == "quit":
        break

    answered += 1

    # Similar-answer matching
    if (
        user_answer == answer
        or answer in user_answer
        or user_answer in answer
    ):
        score += 1
        streak += 1

        if streak > best_streak:
            best_streak = streak

        print("✅ Correct!")
        print(f"🔥 Current Streak: {streak}")

    else:
        print(f"❌ Wrong! Correct Answer: {answer}")
        streak = 0

    print(f"🏆 Score: {score}/{answered}")

    # Round summary
    if (i + 1) % QUESTIONS_PER_ROUND == 0:
        print("\n🎯 ROUND COMPLETE!")
        print(f"Current Score: {score}")
        print(f"🔥 Best Streak So Far: {best_streak}")

print("\n" + "=" * 50)
print("🏆 FINAL RESULTS")
print("=" * 50)

print(f"Questions Answered: {answered}")
print(f"Correct Answers: {score}")
print(f"🔥 Best Streak: {best_streak}")

if answered > 0:
    accuracy = (score / answered) * 100

    print(f"📊 Accuracy: {accuracy:.1f}%")

    if accuracy >= 90:
        grade = "A"
        message = "🌟 Outstanding!"
    elif accuracy >= 75:
        grade = "B"
        message = "🎉 Great Job!"
    elif accuracy >= 50:
        grade = "C"
        message = "👍 Good Effort!"
    else:
        grade = "D"
        message = "📚 Keep Practicing!"

    print(f"🏅 Grade: {grade}")
    print(message)

else:
    print("No questions were answered.")

print("\nThanks for playing! 👋")
