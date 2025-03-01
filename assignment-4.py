import random

def rock_paper_scissors():
    print("""
    =============================================
    Welcome to Rock, Paper, Scissors Game!
    Created by Neha Khan
    =============================================
    """)
    print("Rules: Enter 'rock', 'paper', or 'scissors' to play. Type 'exit' to quit the game.\n")

    # Options for the game
    options = ["rock", "paper", "scissors"]

    while True:
        # Get user input
        user_choice = input("Your choice: ").strip().lower()

        # Check if user wants to exit
        if user_choice == "exit":
            print("Thanks for playing! Goodbye!")
            break

        # Validate user input
        if user_choice not in options:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue

        # Generate computer choice
        computer_choice = random.choice(options)

        # Display choices
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}\n")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a draw!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")

        print("\n--- Let's play again! ---\n")

# Run the game
if __name__ == "__main__":
    rock_paper_scissors()
