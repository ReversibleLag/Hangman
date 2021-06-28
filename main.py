import random


def main():
    running = True
    print("Welcome to Hangman!")
    choice = input("\nReady to play? (y/n) ")

    while running:
        if choice == "y":
            running = True
            hangman()
        else:
            running = False
            exit()


def ran_word():
    words = ["abruptly",
             "absurd",
             "abyss", "affix", "askew", "avenue", "awkward", "axiom", "azure", "bagpipes", "bandwagon", "banjo",
             "bayou", "beekeeper", "bikini", "blitz", "blizzard", "boggle", "bookworm", "boxcar", "boxful", "buckaroo",
             "buffalo", "buffoon", "buxom", "buzzard", "buzzing", "buzzwords", "caliph", "cobweb", "cockiness",
             "croquet", "crypt", "curacao", "cycle", "daiquiri", "dirndl", "disavow", "dizzying", "duplex", "dwarves",
             "embezzle", "equip", "espionage", "euouae", "exodus", "faking", "fishhook", "fixable", "fjord", "flapjack",
             "flopping", "fluffiness", "flyby", "foxglove", "frazzled", "frizzled", "fuchsia", "funny", "gabby",
             "galaxy", "galvanize", "gazebo", "giaour", "gizmo", "glowworm", "glyph", "gnarly", "gnostic", "gossip",
             "grogginess", "haiku", "haphazard", "hyphen", "iatrogenic", "icebox", "injury", "ivory", "ivy", "jackpot",
             "jaundice", "jawbreaker", "jaywalk", "jazziest", "jazzy", "jelly", "jigsaw", "jinx", "jiujitsu", "jockey",
             "jogging", "joking", "jovial", "joyful", "juicy", "jukebox", "jumbo", "kayak", "kazoo", "keyhole", "khaki",
             "kilobyte", "kiosk", "kitsch", "kiwifruit", "klutz", "knapsack", "larynx", "lengths", "lucky", "luxury",
             "lymph", "marquis", "matrix", "megahertz", "microwave", "mnemonic", "mystify", "naphtha", "nightclub",
             "nowadays", "numbskull", "nymph", "onyx", "ovary", "oxidize", "oxygen", "pajama", "peekaboo", "phlegm",
             "pixel", "pizazz", "pneumonia", "polka", "pshaw", "psyche", "puppy", "puzzling", "quartz", "queue",
             "quips", "quixotic", "quiz", "quizzes", "quorum", "razzmatazz", "rhubarb", "rhythm", "rickshaw",
             "schnapps", "scratch", "shiv", "snazzy", "sphinx", "spritz", "squawk", "staff", "strength", "strengths",
             "stretch", "stronghold", "stymied", "subway", "swivel", "syndrome", "thriftless", "thumbscrew", "topaz",
             "transcript", "transgress", "transplant", "triphthong", "twelfth", "twelfths", "unknown", "unworthy",
             "unzip", "uptown", "vaporize", "vixen", "vodka", "voodoo", "vortex", "voyeurism", "walkway", "waltz",
             "wave", "wavy", "waxy", "wellspring", "wheezy", "whiskey", "whizzing", "whomever", "wimpy", "witchcraft",
             "wizard", "woozy", "wristwatch", "wyvern", "xylophone", "yachtsman", "yippee", "yoked", "youthful",
             "yummy", "zephyr", "zigzag", "zigzagging", "zilch", "zipper", "zodiac", "zombie"]

    return random.choice(words)


def dead_man(tries):
    if tries == 0:
        print("----------")
        print("|        |")
        print("|         ")
        print("|         ")
        print("|         ")
        print("|         ")
        print("|         ")
        print("")
    elif tries == 1:
        print("----------")
        print("|        |")
        print("|        O")
        print("|         ")
        print("|         ")
        print("|         ")
        print("|         ")
        print("")
    elif tries == 2:
        print("----------")
        print("|        |")
        print("|        O")
        print("|        |")
        print("|         ")
        print("|         ")
        print("|         ")
        print("")
    elif tries == 3:
        print("----------")
        print("|        |")
        print("|        O")
        print("|        |")
        print("|       / ")
        print("|         ")
        print("|         ")
        print("")
    elif tries == 4:
        print("----------")
        print("|        |")
        print("|        O")
        print("|        |")
        print("|       / \\")
        print("|         ")
        print("|         ")
        print("")
    elif tries == 5:
        print("----------")
        print("|        |")
        print("|        O")
        print("|       /|")
        print("|       / \\")
        print("|         ")
        print("|         ")
        print("")
    elif tries == 6:
        print("----------")
        print("|        |")
        print("|        O")
        print("|       /|\\")
        print("|       / \\")
        print("|         ")
        print("|         ")
        print("")


def hangman():
    running = True
    word = ran_word()

    tries = 0
    total_char = 0
    wrong_letters = []
    length = len(word)

    solved_word = [0] * length
    actual_word = list(word)
    # print(actual_word)
    while running:

        dead_man(tries)

        for i in range(length):
            if solved_word[i] == 1:
                print(f"{actual_word[i]} ", end="")
            else:
                print(f"  ", end="")

        print("")
        print("_ " * length)

        guess = input("\nGuess a letter: ")[0]

        # print(word)

        filled_guess = fill_in(word, guess)
        # print(filled_guess)
        if filled_guess == -1:
            print("Incorrect letter!")
            if not wrong_letters:
                wrong_letters.append(guess)
                tries += 1
            else:
                for i in wrong_letters:
                    if guess in wrong_letters:
                        continue
                    else:
                        wrong_letters.append(guess)
                        tries += 1
        else:
            # print(filled_guess)
            for i in filled_guess:
                if solved_word[i] == 0:
                    solved_word[i] = 1
                    total_char += 1

        print(f"\nWrong letters: {wrong_letters}")

        if total_char == length:
            print(f"You win! The word was {word}")
            choice = input("Play again? (y/n) ")
            if choice == "y":
                running = False
            else:
                exit()
        if tries == 7:
            print(f"You lose! The word was {word}")
            choice = input("Play again? (y/n) ")
            if choice == "y":
                running = False
            else:
                exit()
        # print(filled_spaces)
    hangman()


def fill_in(word, guess):
    filled_spaces = []

    count = 0
    for i in word:
        if i == guess:
            filled_spaces.append(count)
        count += 1

    # print(filled_spaces)
    if not filled_spaces:
        return -1

    return filled_spaces


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
