# CTI-110 P5HW- Math Quiz
# Daniel Chapa
# 5/5/2023
# this program uses loops, functions and module import to create simple math quizzes  
# the program displays two random generated numbers
# asks the user to add the two numbers together
# user enters an answer
# if the answer is correct, a message of congratulations is displayed 
# if the answer is incorrect, the program notifies the user if their answer was too low or too high and ask them to guess again 
# the user guesses until they get the right answer 
# the program keeps track of the number of guesses 
# once the user has made a correct guess, the program then tells the number of guesses it took to get the right answer
# add a subtraction function to subtract the generated random numbers using the same code for adding numbers only subtracting  
# when/if user enters 1, the program is to execute a function that generates the numbers, adds them, asks user to enter an answer and display results
# when/if user enters 2, the program is to execute a function that generates the numbers, subtracts them, asks user to enter an answer and display results
# if/when the user enters 3, the program is to terminate
# if/when user enters anything other than 1, 2, or 3, an error message should display letting the user know, then the menu should display again
# when/if user guesses the right number, congratulate them and display the menu again to give them the option to play again
# the program terminates if user enters 3
# print("Welcome to Math Quiz\n")
# use a while loop for the guesses
# need to count the number of guesses with a counter and print the count
# print("MAIN MENU")
# print("-----------------------------------------------------------")
# print("1. Adding Random Numbers")
# print("2. Subtracting Random Numbers")
# print("3. Exit")
# write a statement "Please choose one of the menu options:"
# put the choices into if and elif statements
# if choice == "1":
# elif choice == "2":
# elif choice == "3":
# print ("Thank you for playing...")
# print ("Bye!!")
#
#
import random

def add_numbers():
    num1 = random.randint(1, 500)
    num2 = random.randint(1, 500)
    answer = num1 + num2
    guess = 0
    count = 0
    while guess != answer:
        print(f" {  num1}\n+{num2}")
        guess = int(input("Enter answer: "))
        count += 1
        if guess < answer:
            print("Sorry, guess is too low.")
        elif guess > answer:
            print("Sorry, guess is too high.")
        else:
            print("Congratulations!!!! Your answer is correct.")
            print("Number of guesses:", count)

def subtract_numbers():
    num1 = random.randint(1, 500)
    num2 = random.randint(1, 500)
    answer = num1 - num2
    guess = 0
    count = 0
    while guess != answer:
        print(f" {  num1}\n-{num2}")
        guess = int(input("Enter answer: "))
        count += 1
        if guess < answer:
            print("Sorry, guess is too low.")
        elif guess > answer:
            print("Sorry, guess is too high.")
        else:
            print("Congratulations!!!! Your answer is correct.")
            print("Number of guesses:", count)

def main_menu():
    print("Welcome to Math Quiz\n")
    while True:
        print("MAIN MENU")
        print("-----------------------------------------------------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit")
        choice = input("\nPlease choose one of the menu options: ")
        if choice == "1":
            add_numbers()
        elif choice == "2":
            subtract_numbers()
        elif choice == "3":
            print("Thank you for playing...")
            print("Bye!!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main_menu()
