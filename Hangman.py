import random

def main():
    lives = 6

    category = input("Choose a category (science, programming, sports): ").lower()

    science = ["biology", "chemistry", "physics", "computing", "economics"]
    programming = ["python", "javascript", "typescript", "swift", "kotlin"]
    sports = ["football", "cricket", "rugby", "volleyball", "tennis", "basketball"]

    hangman_stages = [

        # 6 lives
        """
 +---+
 |   |
     |
     |
     |
     |
=========
""",

        # 5 lives
        """
 +---+
 |   |
 O   |
     |
     |
     |
=========
""",

        # 4 lives
        """
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
""",

        # 3 lives
        """
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
""",

        # 2 lives
        """
 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========
""",

        # 1 life
        """
 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========
""",

        # 0 lives
        """
 +---+
 |   |
 O   |
/|\\  |
/ \\  |
     |
=========
"""
    ]

    if category == "science":
        words = science
    elif category == "programming":
        words = programming
    elif category == "sports":
        words = sports
    else:
        print("Invalid category! Defaulting to science.")
        words = science

    secret_word = random.choice(words)

    displayed_word = ["_"] * len(secret_word)
    guessed_letters = []

    print("\nWelcome to Hangman!")
    print("Guess the hidden word one letter at a time.")
    print(f"You have {lives} lives.")
    print(hangman_stages[0])
    print("Word:", " ".join(displayed_word))

    while "_" in displayed_word and lives > 0:

        guess = input("\nEnter your guess: ").lower()

        if len(guess) != 1:
            print("Please enter only one letter.")
            continue

        if not guess.isalpha():
            print("Please enter a letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct!")

            for i, letter in enumerate(secret_word):
                if letter == guess:
                    displayed_word[i] = guess

        else:
            print("Wrong!")
            lives -= 1

        print(hangman_stages[6 - lives])
        print("Word:", " ".join(displayed_word))
        print("Guessed letters:", ", ".join(guessed_letters))
        print(f"Lives remaining: {lives}")

    if "_" not in displayed_word:
        print("\n🎉 Congratulations!")
        print(f"You guessed the word: {secret_word}")
    else:
        print("\n💀 Game Over!")
        print(f"The secret word was: {secret_word}")


while True:
    main()

    retry = input("\nPlay again? (y/n): ").lower()

    if retry != "y":
        print("Thanks for playing!")
        break
