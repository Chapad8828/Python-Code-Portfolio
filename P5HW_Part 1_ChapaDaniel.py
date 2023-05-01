# This program uses loops, functions and module import to create simple math quizzes.  
# The program displays two random generated numbers
# User enters an answer
# If the answer is correct, a message of congratulations is displayed. 
# If the answer is incorrect, the program notifies the user if their answer was too low or too high and ask them to guess again. 
# The user guesses until they get the right answer. 
# The program keeps track of the number of guesses. 
# Once the user has made a correct guess, the program then tells the number of guesses it took to get the right answer.
# CTI-110 P5HW- Math Quiz
# Daniel Chapa
# 4/26/2023
#
import random

def generate_numbers():
    """Generate two random numbers between 1 and 500."""
    num1 = random.randint(1, 500)
    num2 = random.randint(1, 500)
    return num1, num2

def add_numbers(num1, num2):
    """Add two numbers and return the sum."""
    return num1 + num2

def quiz():
    """Run a math quiz."""
    num1, num2 = generate_numbers()
    answer = add_numbers(num1, num2)
    guesses = 0
    while True:
        print(" ",num1)
        print("+",num2)
        guess = input("Enter your answer: ")
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid number.")
            continue
        guesses += 1
        if guess == answer:
            print("Congratulations! You got the answer in", guesses, "guesses.")
            break
        elif guess < answer:
            print("Your answer is too low. Guess again.")
        else:
            print("Your answer is too high. Guess again.")
        
if __name__ == '__main__':
    quiz()
