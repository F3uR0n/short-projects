import random
from hangman_arts import stages
from hangman_arts import logo

print(logo)
print("Welcome to Hangman!! Ready to Hang??")

word_list = ['rank', 'champion', 'camel']
computer_choice= random.choice(word_list)
word_length= len(computer_choice)

end_of_games= False
lives= 6
display=[]

for _ in range(word_length):
    display += "_"
print(display)

while not end_of_games:
    user_choice = input("Guess the letter: \n").lower()
    if user_choice in display:
        print(f"You have already guessed {user_choice}")
    for position in range(word_length):
        letter = computer_choice[position]
        if letter== user_choice:
            display[position]= letter
    if user_choice not in computer_choice:
        print(f"You guessed {user_choice}, that's not in the word. You lose a life.")
        lives -=1
        if lives == 0:
            end_of_games= True
            print("You Loose")
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_games= True
        print("You Win")
    print(stages[lives])