from game_data import data
import random
import sys
import subprocess
from art import logo, vs


def data_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def compare(guess, a_follower_account, b_follower_account):
    if a_follower_account > b_follower_account:
        return guess == "a"
    else:
        return guess == "b"


def clear_screen():
    operating_sys = sys.platform
    if operating_sys == 'win32':
        subprocess.run('cls', shell=True)
    elif operating_sys == 'linux' or operating_sys == 'darwin':
        subprocess.run('clear', shell=True)


print(logo)
score = 0
you_are_right = True
account_b = random.choice(data)
while you_are_right:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {data_data(account_a)}")
    print(vs)
    print(f"Compare B: {data_data(account_b)}")

    guess = input("Who has more followers, Account A or B: ").lower()
    a_follower_account = account_a["follower_count"]
    b_follower_account = account_b["follower_count"]
    correct_answer = compare(guess, a_follower_account, b_follower_account)
    clear_screen()
    print(logo)

    if correct_answer:
        score += 1
        print(f"You're Correct, Your Score is {score}")
    else:
        you_are_right = False
        print(f"You're wrong. Your Final Score is {score}")
