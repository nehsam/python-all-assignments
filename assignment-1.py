def alien_adventure():
    print("""
    ================================================
    Welcome to Alien Adventure! --- created by [NEHA KANWAL]
    ================================================
    """)
    print("Let's create a fun space adventure story. Just answer a few questions!\n")

    # User Inputs
    print("=== Step 1: Provide a Planet Name ===")
    planet = input("Enter the name of a planet (e.g., Mars, Jupiter, Pandora): ")

    print("\n=== Step 2: Provide a Job Title ===")
    job = input("Enter a job title (e.g., scientist, explorer, chef): ")

    print("\n=== Step 3: Provide an Alien Name ===")
    alien_name = input("Enter a funny alien name (e.g., Zork, Blipblop, Zorg): ")

    print("\n=== Step 4: Provide a Space Object ===")
    space_object = input("Enter a space object (e.g., comet, asteroid, spaceship): ")

    print("\n=== Step 5: Provide an Emotion ===")
    emotion = input("Enter an emotion (e.g., happy, scared, excited): ")

    # Create the story using f-strings
    story = f"""
    One day, a {job} was exploring the planet {planet}. 
    Suddenly, they met an alien named {alien_name}, who was holding a {space_object}.
    "{alien_name}" seemed very {emotion} and started jumping around.
    Together, they decided to build a spaceship and travel across the galaxy.
    It was the beginning of an unforgettable adventure on {planet}!
    """

    # Print the final story
    print("\nHere's your Alien Adventure story:\n")
    print(story)

# Run the game
alien_adventure()
