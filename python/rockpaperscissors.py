import random

options=['rock', 'paper', 'scissors']
player1=input("Player 1, enter your choice:")
compchoice=random.randint(0,2)
compchoice=options[compchoice]



if player1 == 'rock':
    print("Player 1: Rock")


    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

elif player1 == 'paper':
    print("Player 1: Paper")
# Paper
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

elif player1 == 'scissors':
    print("Player 1: Scissors")
# Scissors
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    
if compchoice == 'rock':
    print("Computer: Rock")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")


elif compchoice == 'paper':
    print("Computer: Paper")
# Paper
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

elif compchoice == 'scissors':
    print("Computer: Scissors")
# Scissors
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
    
if player1=='rock' and compchoice=='paper':
    print("Computer Wins")
elif player1=='paper' and compchoice=='scissors':
    print("Computer Wins")
elif player1=='rock' and compchoice=='scissors':
    print("Player Wins")
elif player1=='paper' and compchoice=='rock':
    print("Player wins")
elif player1==compchoice:
    print("Tie")