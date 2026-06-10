import random
import string

print("=" * 50)
print("🔐 ADVANCED PASSWORD GENERATOR")
print("=" * 50)

length = int(input("Enter password length: "))

use_letters = input("Include letters? (y/n): ").lower()
use_numbers = input("Include numbers? (y/n): ").lower()
use_symbols = input("Include symbols? (y/n): ").lower()

characters = ""

if use_letters == "y":
    characters += string.ascii_letters

if use_numbers == "y":
    characters += string.digits

if use_symbols == "y":
    characters += string.punctuation

if characters == "":
    print("❌ Error: You must choose at least one character type.")

else:
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    print("\n🔑 Generated Password:")
    print(password)

    save = input("\nWould you like to save this password? (y/n): ").lower()

    if save == "y":
        website = input("Enter Website/App Name: ")

        with open("passwords.txt", "a") as file:
            file.write(f"{website}: {password}\n")

        print("✅ Password saved successfully!")

    print("\n🎉 Thank you for using the Password Generator!")
