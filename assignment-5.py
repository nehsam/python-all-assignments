import random

def hangman():
    print("""
    =============================================
    Welcome to the Hangman Game!
    Created by Neha Khan
    =============================================
    """)
    print("Rules: You have limited guesses to figure out the word. Good luck!\n")

    # List of possible words
    word_list = ['python', 'hangman', 'developer', 'coding', 'project']
    secret_word = random.choice(word_list)
    guessed_word = ['_'] * len(secret_word)
    guessed_letters = set()
    attempts = 6  # Number of allowed incorrect guesses

    print("Your word: " + " ".join(guessed_word))
    print(f"You have {attempts} attempts remaining.\n")

    while attempts > 0:
        guess = input("Enter a letter: ").lower()

        # Validate user input
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.\n")
            continue

        # Check if the letter was already guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again!\n")
            continue

        # Add the guess to the guessed letters set
        guessed_letters.add(guess)

        # Check if the guessed letter is in the word
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.\n")
            for i, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"Oops! '{guess}' is not in the word. You have {attempts} attempts remaining.\n")

        # Display the current state of the word
        print("Your word: " + " ".join(guessed_word) + "\n")

        # Check if the user has guessed the word
        if '_' not in guessed_word:
            print(f"Congratulations! You guessed the word '{secret_word}' correctly!")
            break
    else:
        print(f"Sorry, you're out of attempts. The word was '{secret_word}'. Better luck next time!")

    print("\nThanks for playing Hangman!")

# Run the game
if __name__ == "__main__":
    hangman()
