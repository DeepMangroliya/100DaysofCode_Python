from art import logo
import random

EASY_LEVEL = 10
HARD_LEVEL = 5

def assign_attempts(difficulty):
    if difficulty == 'hard':
        return HARD_LEVEL
    elif difficulty == 'easy':
        return EASY_LEVEL
    else:
        print("You entered invalid difficulty, Game Over! 😤")

def check_answer(guess, answer):
    if answer < guess:
        print("Too high.")
    elif answer > guess:
        print("Too low.")
    else:
        print("You got it right! You won 😀")
        return True
    print("Guess again.")

def guess_the_number(attempts, answer):
    while attempts:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))

        result = check_answer(guess, answer)
        attempts-=1

    if not result:
        print("You've run out of guesses, you lose.")
        return


def game():
    print (logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    answer = random.randint(1,100)
    print(f"Pssst, the correct answer is {answer}")
    attempts = assign_attempts(difficulty)
    guess_the_number(attempts, answer)

game()