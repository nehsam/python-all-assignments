import random

# Function to run the Guess the Word game
def guess_the_word():
    print("""
    ================================================================
        Welcome to Neha Khan's Guess the Word Game (AI Mode)!
    ================================================================
    Created with 💡 and 💖 by Neha Khan
    Think of a word from the list, and I'll try to guess it!
    ================================================================
    """)
    
    # List of possible words
    words = ['apple', 'banana', 'grape', 'mango', 'peach']
    print(f"I can guess from this list: {words}")
    print("Think of a word from this list, and I'll try to guess it!")

    # Initialize variables
    possible_words = words[:]
    feedback = ""

    while feedback != "c":
        if not possible_words:
            print("\n🤔 Hmm, it seems I ran out of guesses. Did you give me correct feedback?")
            break

        # AI's guess (random choice from the remaining words)
        guess = random.choice(possible_words)
        feedback = input(f"Is your word '{guess}'? (Enter 'h' if it's not in the list, 'l' to remove it, or 'c' if it's correct): ").strip().lower()

        # Handle feedback
        if feedback == "h":
            print("Hmm, I think you're trying to confuse me! Please pick a word from the list.")
        elif feedback == "l":
            possible_words.remove(guess)
            print(f"Okay, I'll remove '{guess}' from my list and try again.")
        elif feedback == "c":
            print(f"\n🎉 Yay! I guessed your word '{guess}' correctly! 🎉")
        else:
            print("⚠️ Invalid input. Please enter 'h', 'l', or 'c'.")

    print("\n✨ Thanks for playing Neha Khan's Guess the Word Game! ✨")

# Run the game
if __name__ == "__main__":
    guess_the_word()
