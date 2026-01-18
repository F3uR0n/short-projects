from random import randint
from art import logo

EASY_LEVEL= 10
HARD_LEVEL= 5
def difficulty():
    level= input("Select the difficulty, easy or hard: ")
    if level=="easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def check_answer(answer, guess, turn):
    if guess>answer:
        print("too high")
        return turn - 1
    elif guess<answer:
        print("too low")
        return turn - 1
    else:
        print(f"You win. The answer is {answer}")
def game():
    print(logo)
    print("Welcome! Guess the number")
    print("I am guessing a number between 1 to 100")
    answer= randint(1, 100)
    turn= difficulty()
    guess= 0
    while guess!=answer:
        guess= int(input("Guess a number: "))
        turn= check_answer(answer, guess, turn)
        print(f"You have {turn} attempts remaining to guess the correct answer")
        if turn==0:
            print("You've run out of guesses, you loose!!")
            return
game()