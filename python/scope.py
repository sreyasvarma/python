#guess game

import random

n=random.randint(1,100)

print("Welcome to number guessing game")

level=input("Choose a difficulty easy or hard 'e' or 'h' ?")
if level=='e':
    print("You have 10 attempts to guess the number")
    attempts=10
elif level=='h':
    print("You have 5 attempts to guess the number")
    attempts=5

while attempts!=0:
    guess=int(input("Enter your guess: "))
    if guess>n:
        print(f"Your guess {guess} is too high")
        attempts-=1
        print(f"you have {attempts} attempts left")
    elif guess<n:
        print(f"Your guess {guess} is too low")
        attempts-=1
        print(f"you have {attempts} attempts left")
    elif guess==n:
        print("You guessed it right")
        print("You win!!!!!!!!!!!!!!!!!!!!!")
        break
    
if attempts==0:
    print("Better luck next time. You lose!!")
    print(f"The number is {n}")
