print("Welcome to the Number Guessing Game!") 

print("I'm thinking of a number between 1 and 100.") 

# The secret number 

secret_number = 42 

# Maximum number of attempts 

max_attempts = 5 

attempts = 0 

# Game 100p 

while attempts < max_attempts:
    attempts = attempts + 1 
    print("Attempt " , attempts , " of " , max_attempts) 

# Get user's guess 

    guess = int(input("Enter your guess: "))
    
# Check if the guess is correct 

    if guess == secret_number: 

        print("Congratulations! You guessed the number!") 

        break 

    elif guess < secret_number: 
        print("Too low! Try again.") 

    else: 
        print("Too high! Try again.") 
