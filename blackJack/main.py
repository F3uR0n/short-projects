print("Welcome To BlackJack")
import random
from Art import logo

def deal_card():
    cards= [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card= random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
def compare(user_score, computer_score):
    if user_score==computer_score:
        return "draw"
    elif computer_score==0:
        return "You Loose, opponent has Blackjack"
    elif user_score==0:
        return "Win with a Blackjack"
    elif user_score>21:
        return "You Loose!! You went over."
    elif computer_score>21:
        return "Opponent went over. You win"
    elif user_score>computer_score:
        return "You Win!!"
    else:
        return "You Loose -_-"
def play_game():
    print(logo)
    user_cards=[]
    computer_cards=[]
    is_game_over=False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"Your Cards {user_cards}, Current Score{user_score}")
        print(f"Computers First Card: {computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_next_card= input("Type y for another card else type n: ")
            if user_next_card=="y":
                user_cards.append(deal_card())
            else:
                is_game_over= True
    while computer_score !=0 and computer_score<17:
        computer_cards.append(deal_card())
        computer_score= calculate_score(computer_cards)

    print(f"Your Final Hand {user_cards}, Final Score: {user_score}")
    print(f"Computer's Final Hand {computer_cards}, Final Score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play Blackjack again, if yes press y else n: ")== "y":
    play_game()