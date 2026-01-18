import random

Rock= """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper= """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

Scissors= """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

game_images= [Rock, Paper, Scissors]
user_choice= int(input("What do you choose, press 0 for Rock, 1 for Paper and 2 for Scissors\n"))
print(f"User Choose {user_choice}")
print(game_images[user_choice])
int_user_choice= int(user_choice)
computer_choice= random.randint(0, 2)
print(f"Computer Choose {computer_choice}")
print(game_images[computer_choice])

if int_user_choice == computer_choice:
    print("Its Draw")
elif (int_user_choice==0) and (computer_choice==1):
    print("Computer Wins")
elif (int_user_choice==0) and (computer_choice==2):
    print("User Wins")
elif (int_user_choice==1) and (computer_choice==2):
    print("Computer Wins")
elif (computer_choice==0) and (int_user_choice==1):
    print("User Wins")
elif (computer_choice==0) and (int_user_choice==2):
    print("Computer Wins")
elif (computer_choice==1) and (int_user_choice==2):
    print("User Wins")
else:
    print("Invalid Choice")
