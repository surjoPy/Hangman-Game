import random


def main():

    lives = 6

    # =========================
    # CATEGORY LISTS
    # =========================

    easy = ["animals", "food", "sports", "countries", "school"]

    medium = ["technology", "science", "geography", "football", "nature"]

    hard = ["programming", "physics", "medicine", "astronomy", "engineering"]


    # =========================
    # WORD LISTS
    # =========================

    easy_categories = {
        "animals": ["cat", "dog", "lion", "tiger", "horse"],
        "food": ["pizza", "bread", "apple", "burger", "cheese"],
        "sports": ["football", "tennis", "cricket", "rugby", "boxing"],
        "countries": ["india", "japan", "china", "nepal", "egypt"],
        "school": ["math", "science", "english", "history", "music"]
    }

    medium_categories = {
        "technology": ["computer", "keyboard", "internet", "software", "network"],
        "science": ["biology", "physics", "chemistry", "gravity", "molecule"],
        "geography": ["mountain", "desert", "island", "volcano", "continent"],
        "football": ["goalkeeper", "midfielder", "striker", "stadium", "penalty"],
        "nature": ["elephant", "giraffe", "penguin", "rainforest", "sunflower"]
    }

    hard_categories = {
        "programming": ["javascript", "typescript", "algorithm", "framework", "compiler"],
        "physics": ["relativity", "quantum", "electromagnetism", "momentum", "wavelength"],
        "medicine": ["diagnosis", "antibiotic", "infection", "skeleton", "respiratory"],
        "astronomy": ["supernova", "blackhole", "asteroid", "exoplanet", "constellation"],
        "engineering": ["electronics", "mechanical", "aerospace", "thermodynamics", "semiconductor"]
    }


    # =========================
    # HINT DICTIONARIES
    # =========================

    animals_hints = {
        "cat": "A common household pet that meows",
        "dog": "A loyal household animal that barks",
        "lion": "A large wild cat known as the king of the jungle",
        "tiger": "A large striped wild cat",
        "horse": "An animal commonly used for riding"
    }

    food_hints = {
        "pizza": "A popular dish with a baked dough base and toppings",
        "bread": "A baked food commonly made from flour",
        "apple": "A round fruit that can be red, green, or yellow",
        "burger": "A sandwich usually containing a meat patty",
        "cheese": "A dairy food made from milk"
    }

    sports_hints = {
        "football": "A sport where players try to score goals",
        "tennis": "A racket sport played over a net",
        "cricket": "A bat-and-ball sport popular in many countries",
        "rugby": "A contact sport played with an oval-shaped ball",
        "boxing": "A combat sport involving punches"
    }

    countries_hints = {
        "india": "A large country in South Asia",
        "japan": "An island country in East Asia",
        "china": "A large country in East Asia",
        "nepal": "A country home to Mount Everest",
        "egypt": "A country famous for its ancient pyramids"
    }

    school_hints = {
        "math": "The study of numbers, shapes, and patterns",
        "science": "The systematic study of the natural world",
        "english": "A language and a school subject",
        "history": "The study of events from the past",
        "music": "The art of organized sound"
    }


    technology_hints = {
        "computer": "An electronic machine used to process information",
        "keyboard": "A device used to enter text into a computer",
        "internet": "A worldwide network connecting computers",
        "software": "Programs and instructions that run on a computer",
        "network": "A group of connected computers or devices"
    }

    science_hints = {
        "biology": "The study of living organisms",
        "physics": "The study of matter, energy, and forces",
        "chemistry": "The study of substances and their reactions",
        "gravity": "The force that attracts objects toward each other",
        "molecule": "Two or more atoms chemically bonded together"
    }

    geography_hints = {
        "mountain": "A large natural elevation of Earth's surface",
        "desert": "A very dry area that receives little rainfall",
        "island": "Land completely surrounded by water",
        "volcano": "An opening in Earth's crust that can release lava",
        "continent": "One of Earth's large continuous landmasses"
    }

    football_hints = {
        "goalkeeper": "The player who protects the goal",
        "midfielder": "A player who usually plays in the middle of the field",
        "striker": "A forward who often scores goals",
        "stadium": "A large venue where football matches are played",
        "penalty": "A free shot awarded after certain fouls"
    }

    nature_hints = {
        "elephant": "The largest living land animal",
        "giraffe": "The tallest living land animal",
        "penguin": "A flightless bird commonly associated with Antarctica",
        "rainforest": "A dense forest with very high rainfall",
        "sunflower": "A tall plant known for its large yellow flower"
    }


    programming_hints = {
        "javascript": "A programming language commonly used for web development",
        "typescript": "A programming language that extends JavaScript with static typing",
        "algorithm": "A step-by-step procedure for solving a problem",
        "framework": "A reusable structure used to build software",
        "compiler": "A program that translates source code into another form"
    }

    physics_hints = {
        "relativity": "Einstein's theory concerning space, time, and gravity",
        "quantum": "Relating to the smallest discrete amounts of physical quantities",
        "electromagnetism": "The interaction between electric and magnetic fields",
        "momentum": "A quantity related to an object's mass and velocity",
        "wavelength": "The distance between corresponding points on a wave"
    }

    medicine_hints = {
        "diagnosis": "The identification of a disease or medical condition",
        "antibiotic": "A medicine used to treat certain bacterial infections",
        "infection": "The invasion of the body by harmful microorganisms",
        "skeleton": "The framework of bones supporting the body",
        "respiratory": "Related to breathing and the respiratory system"
    }

    astronomy_hints = {
        "supernova": "A powerful explosion marking the death of some stars",
        "blackhole": "An object with gravity so strong that light cannot escape",
        "asteroid": "A rocky object that orbits the Sun",
        "exoplanet": "A planet that orbits a star outside our Solar System",
        "constellation": "A recognized pattern of stars in the night sky"
    }

    engineering_hints = {
        "electronics": "The study and use of circuits and electronic devices",
        "mechanical": "Related to machines, motion, and mechanical systems",
        "aerospace": "The field involving aircraft and spacecraft",
        "thermodynamics": "The study of heat, energy, and their transformations",
        "semiconductor": "A material with electrical conductivity between a conductor and insulator"
    }


    # =========================
    # HANGMAN STAGES
    # =========================

    hangman_stages = [

        """
 +---+
 |   |
     |
     |
     |
     |
=========
""",

        """
 +---+
 |   |
 O   |
     |
     |
     |
=========
""",

        """
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
""",

        """
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
""",

        """
 +---+
 |   |
 O   |
/|\\  |
     |
     |
=========
""",

        """
 +---+
 |   |
 O   |
/|\\  |
/    |
     |
=========
""",

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


    # =========================
    # DIFFICULTY
    # =========================

    difficulty = input(
        "Please enter the difficulty (easy, medium, hard): "
    ).lower()


    # =========================
    # EASY
    # =========================

    if difficulty == "easy":

        print("Available categories:", easy)

        while True:

            category = input("Please enter the category: ").lower()

            if category in easy:

                words = easy_categories[category]

                secret_word = random.choice(words)

                break

            else:

                print("Invalid category! Try again.")


    # =========================
    # MEDIUM
    # =========================

    elif difficulty == "medium":

        print("Available categories:", medium)

        while True:

            category = input("Please enter the category: ").lower()

            if category in medium:

                words = medium_categories[category]

                secret_word = random.choice(words)

                break

            else:

                print("Invalid category! Try again.")


    # =========================
    # HARD
    # =========================

    elif difficulty == "hard":

        print("Available categories:", hard)

        while True:

            category = input("Please enter the category: ").lower()

            if category in hard:

                words = hard_categories[category]

                secret_word = random.choice(words)

                break

            else:

                print("Invalid category! Try again.")


    # =========================
    # INVALID DIFFICULTY
    # =========================

    else:

        print("Invalid difficulty!")

        category = random.choice(medium)

        print(f"The category '{category}' has been randomly selected.")

        words = medium_categories[category]

        secret_word = random.choice(words)

        difficulty = "medium"


    # =========================
    # GET THE HINT
    # =========================

    if category == "animals":
        hint = animals_hints[secret_word]

    elif category == "food":
        hint = food_hints[secret_word]

    elif category == "sports":
        hint = sports_hints[secret_word]

    elif category == "countries":
        hint = countries_hints[secret_word]

    elif category == "school":
        hint = school_hints[secret_word]

    elif category == "technology":
        hint = technology_hints[secret_word]

    elif category == "science":
        hint = science_hints[secret_word]

    elif category == "geography":
        hint = geography_hints[secret_word]

    elif category == "football":
        hint = football_hints[secret_word]

    elif category == "nature":
        hint = nature_hints[secret_word]

    elif category == "programming":
        hint = programming_hints[secret_word]

    elif category == "physics":
        hint = physics_hints[secret_word]

    elif category == "medicine":
        hint = medicine_hints[secret_word]

    elif category == "astronomy":
        hint = astronomy_hints[secret_word]

    elif category == "engineering":
        hint = engineering_hints[secret_word]


    # =========================
    # START GAME
    # =========================

    displayed_word = ["_"] * len(secret_word)

    guessed_letters = []

    print("\nWelcome to Hangman!")
    print(f"Difficulty: {difficulty}")
    print(f"Category: {category}")
    print(f"Hint: {hint}")
    print(f"You have {lives} lives.")

    print(hangman_stages[0])

    print("Word:", " ".join(displayed_word))


    # =========================
    # GAME LOOP
    # =========================

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


    # =========================
    # GAME RESULT
    # =========================

    if "_" not in displayed_word:

        print("\n🎉 Congratulations!")

        print(f"You guessed the word: {secret_word}")

    else:

        print("\n💀 Game Over!")

        print(f"The secret word was: {secret_word}")


# =========================
# PLAY AGAIN
# =========================

while True:

    main()

    retry = input("\nPlay again? (y/n): ").lower()

    if retry != "y":

        print("Thanks for playing!")

        break
