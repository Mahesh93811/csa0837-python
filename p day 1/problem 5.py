def guess_number_game():
    # Manually setting a random number for demonstration (you can change this)
    number_to_guess = 56  # Let's assume the number to guess is 56
    attempts = 0
    guessed = False

    print("Guess a number between 1 and 100.")

    while not guessed:
        
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < number_to_guess:
            print("Higher!")
        elif user_guess > number_to_guess:
            print("Lower!")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
            guessed = True

guess_number_game()
