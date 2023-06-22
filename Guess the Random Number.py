# TODO: Import the random module
import random
random.seed(900)

def number_guess(num):
    # TODO: Get a random number between 1-100
    guess = random.randint(1,100)
    # TODO: Compare parameter num to the random number
    if num == guess:
        print(f'{num} is correct!')
    elif guess > num:
        print(f'{num} is too low. Random number was {guess}.')
    else:
        print(f'{num} is too high. Random number was {guess}.')
        
if __name__ == "__main__":
    # Use the seed 900 to get the same pseudo random numbers every time
    random.seed(900)
    
    user_input = input()
    tokens = user_input.split()
    for token in tokens:
        # Convert the string tokens into integers
        num = int(token)
        number_guess(num)
