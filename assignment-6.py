import time

def countdown_timer():
    print("""
    =============================================
    Welcome to the Countdown Timer!
    Created by Neha Khan
    =============================================
    """)

    # Get user input for the countdown time
    while True:
        try:
            total_seconds = int(input("Enter the countdown time in seconds: "))
            if total_seconds <= 0:
                print("Please enter a positive number.\n")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer value.\n")

    print(f"\nCountdown starts now for {total_seconds} seconds!\n")
    time.sleep(1)  # Pause before countdown begins

    # Countdown logic
    while total_seconds > 0:
        minutes, seconds = divmod(total_seconds, 60)
        timer_display = f"{minutes:02}:{seconds:02}"
        print(f"Time Remaining: {timer_display}", end="\r")
        time.sleep(1)  # Pause for one second
        total_seconds -= 1

    print("\nTime's up! Your countdown is complete.")
    print("\nThank you for using the Countdown Timer!")

# Run the countdown timer
if __name__ == "__main__":
    countdown_timer()
