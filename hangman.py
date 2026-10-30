import subprocess
import random
import time
import re
import os


def clear_screen():
    if os.name == "nt":
        subprocess.run("cls", shell=True)
    else:
        subprocess.run("clear")

def print_title():
    print("###################\n"
          "#  H_A_N_G_M_A_N  #\n"
          "###################\n")

def print_progress(allowed_incorrect_guesses,
                    category,
                    incorrect_guess,
                    correct_guesses_letters,
                    incorrect_guesses_letters,
                    working_letters_list,
                    word):
    for character in working_letters_list:
        correct_guesses_letters += character
        correct_guesses_letters += " "

    print(f"Remaining incorrect guesses: {allowed_incorrect_guesses - incorrect_guess}")
    print(f"Word category: {category.capitalize()}")
    print(f"Word length: {len(word)} characters\n")
    print(f"Progress: {correct_guesses_letters}")
    print(f"Incorrect guesses: {incorrect_guesses_letters}\n")
    correct_guesses_letters = ""

words_dictionary = {
    "fruits": [
        "apple", "banana", "orange", "grape", "strawberry",
        "blueberry", "raspberry", "blackberry", "watermelon", "cantaloupe",
        "honeydew", "pineapple", "mango", "papaya", "kiwi",
        "peach", "pear", "plum", "cherry", "apricot", "clementine",
        "nectarine", "pomegranate", "fig", "date", "coconut",
        "lemon", "lime", "grapefruit", "tangerine", "mandarin",
        "avocado", "guava", "lychee", "breadfruit", "plantain",
        "jackfruit", "durian", "persimmon", "cranberry", "gooseberry",
        "mulberry", "starfruit", "quince", "elderberry", "boysenberry",
        "longan", "kumquat"
    ],

    "vegetables": [
        "carrot", "broccoli", "spinach", "potato", "kohlrabi",
        "tomato", "cucumber", "lettuce", "cabbage", "cauliflower",
        "onion", "garlic", "pepper", "zucchini", "endive",
        "eggplant", "pumpkin", "radish", "beetroot", "turnip",
        "parsnip", "celery", "asparagus", "artichoke",
        "kale", "arugula", "watercress", "leek", "shallot",
        "bean", "pea", "corn", "okra", "fennel", "daikon",
        "squash", "yam", "cassava", "taro", "mushroom",
        "jicama", "rutabaga"
    ],

    "animals": [
        "lion", "tiger", "elephant", "giraffe", "zebra",
        "leopard", "cheetah", "wolf", "fox", "bear",
        "panda", "koala", "kangaroo", "wallaby", "monkey",
        "gorilla", "chimpanzee", "orangutan", "baboon", "deer",
        "moose", "elk", "bison", "buffalo", "horse",
        "donkey", "cow", "bull", "sheep", "goat",
        "pig", "boar", "rabbit", "hare", "squirrel",
        "chipmunk", "beaver", "otter", "badger", "raccoon",
        "skunk", "hedgehog", "porcupine", "mouse", "rat",
        "hamster", "bat", "dog", "cat",
        "hyena", "hippopotamus", "rhinoceros", "camel", "llama",
        "alpaca", "sloth", "anteater", "armadillo", "platypus",
        "dolphin", "whale", "shark", "octopus", "squid",
        "jellyfish", "starfish", "crab", "lobster", "shrimp",
        "crocodile", "alligator", "turtle", "tortoise", "snake",
        "lizard", "chameleon", "iguana", "frog", "toad",
        "salamander", "eagle", "hawk", "falcon", "owl",
        "parrot", "penguin", "ostrich", "peacock", "flamingo",
        "swan", "duck", "goose", "chicken", "turkey",
        "pigeon", "sparrow", "woodpecker"
    ]
}

keep_playing = "Y"
correct_guesses_letters = ""
incorrect_guesses_letters = ""

# Main loop
while keep_playing == "Y":
    
    # Prepare a random word from a random category.
    category = random.choice(list(words_dictionary.keys()))
    category_list = words_dictionary[category]
    word = random.choice(category_list).upper()

    player_guess = ""
    letter_index = 0
    incorrect_guess = 0

    word_letters_list = []
    working_letters_list = []
    correct_guesses_letters = ""
    incorrect_guesses_letters = ""

    # Allow player to configure number of incorrect guesses.
    while True:
        clear_screen()
        print_title()
        allowed_incorrect_guesses = input("How many incorrect guesses is the player allowed to make?\n" \
                                "Pick from 1 to 10: ")

        if re.fullmatch(r"([1-9]|10)", allowed_incorrect_guesses, re.IGNORECASE):
            allowed_incorrect_guesses = (int(allowed_incorrect_guesses))
            break
        else:
            print("Invalid input!")
            time.sleep(1)

    # Prepare list of empty spaces for characters in word
    for letter in word:
        working_letters_list.append("_")

    # Prepare list of characters in word
    for letter in word:
        word_letters_list.append(letter)

    # Print progress
    clear_screen()
    print_title()
    print_progress(allowed_incorrect_guesses,
                    category,
                    incorrect_guess,
                    correct_guesses_letters,
                    incorrect_guesses_letters,
                    working_letters_list, 
                    word)

    # Secondary game loop that checks if win condition has been met.
    while working_letters_list != word_letters_list:

        # Allow player to pick a letter and regex validate input.
        while True:
            player_guess = input("Pick a letter: ")
    
            if re.fullmatch(r"[a-zA-Z]", player_guess, re.IGNORECASE):
                player_guess = player_guess.upper()
                break
            else:
                clear_screen()
                print_progress(allowed_incorrect_guesses,
                                category,
                                incorrect_guess,
                                correct_guesses_letters,
                                incorrect_guesses_letters,
                                working_letters_list, 
                                word)
                print("Invalid input")
                time.sleep(1)

        # Check if player guess is contained within word
        if player_guess in word:
            print("\nCorrect!\n")

            letter_index = 0

            # Find letter_index of player guess in word and replace blanks with player_guess
            while True:
                letter_index = word.find(player_guess, letter_index)

                if letter_index == -1:
                    break

                working_letters_list[letter_index] = player_guess        
                letter_index += 1

            # Print progress to terminal
            clear_screen()
            print_title()
            print_progress(allowed_incorrect_guesses,
                            category,
                            incorrect_guess,
                            correct_guesses_letters,
                            incorrect_guesses_letters,
                            working_letters_list, 
                            word)
            
        # Count incorrect guesses and stop the game when limit is reached
        else:
            print("\nIncorrect!\n")
            incorrect_guess += 1
            if player_guess not in incorrect_guesses_letters:
                incorrect_guesses_letters += player_guess

            # Print progress to terminal
            clear_screen()
            print_title()
            print_progress(allowed_incorrect_guesses,
                           category,
                           incorrect_guess,
                           correct_guesses_letters,
                           incorrect_guesses_letters,
                           working_letters_list, 
                           word)

            if incorrect_guess == allowed_incorrect_guesses:
                clear_screen()
                print_title()
                print("You lost!")
                print(f"The word was: {word}")
                time.sleep(2)
                break

    if working_letters_list == word_letters_list:
        clear_screen()
        print_title()
        print("You won!")
        time.sleep(2)

    while True:
        clear_screen()
        print_title()
        keep_playing = input("Play again? (Y/N): ")

        if re.fullmatch(r"[yn]", keep_playing, re.IGNORECASE):
            keep_playing = keep_playing.upper()
            break
        else:
            clear_screen()
            print_title()
            print("Play again? (Y/N): ")
            print("Invalid input")
            time.sleep(1)

clear_screen()
