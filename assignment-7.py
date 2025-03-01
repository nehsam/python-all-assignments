import random
import string

def password_generator():
    print("""
    =======================================================
    Welcome to the Random Password Generator!
    Created by Neha Khan
    =======================================================
    """)

    # Get user input for the number of passwords and their length
    while True:
        try:
            num_passwords = int(input("How many passwords would you like to generate? "))
            password_length = int(input("Enter the desired password length: "))
            if num_passwords <= 0 or password_length <= 0:
                print("Please enter positive numbers only.\n")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter integer values only.\n")

    # Define the characters to use in the passwords
    characters = string.ascii_letters + string.digits + string.punctuation

    print("\nGenerating passwords...\n")

    # Generate passwords
    for i in range(num_passwords):
        password = ''.join(random.choice(characters) for _ in range(password_length))
        print(f"Password {i + 1}: {password}")

    print("\nYour passwords have been generated! Thank you for using the Password Generator.")

# Run the password generator
if __name__ == "__main__":
    password_generator()
