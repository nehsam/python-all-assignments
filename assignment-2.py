import random

# Function to run the Guess the Word game
def guess_the_word():
    print("""
    ================================================
        Welcome to Neha Khan's Guess the Word Game!
    ================================================
    Created with 💖 by Neha Khan - Let's have fun!
    ================================================
    """)
    print("I am thinking of a word from this list: ['apple', 'banana', 'grape', 'mango', 'peach']")
    
    # List of words
    words = ['apple', 'banana', 'grape', 'mango', 'peach']
    secret_word = random.choice(words)
    attempts = 0

    while True:
        # Get user's guess
        guess = input("Enter your guess: ").strip().lower()
        attempts += 1

        # Check if the guess is correct
        if guess == secret_word:
            print(f"\n🎉 Congratulations! You guessed the word '{secret_word}' in {attempts} attempts. 🎉")
            break
        else:
            print("❌ Wrong guess! Try again.")

    print("\nGame Over. Thanks for playing Neha's Guess the Word Game!")

# Start the game
guess_the_word()
