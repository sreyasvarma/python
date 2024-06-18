#blackjackgame
import random

cardvalues=[11,2,3,4,5,6,7,8,9,10,10,10,10]

comp=[]
user=[]
def dealcard():
    card1=random.choice(cardvalues)
    user.append(card1)
    card2=random.choice(cardvalues)
    comp.append(card2)

dealcard()
dealcard()

usersum=user[0]+user[1]
compsum=comp[0]+comp[1]

#print(f"{user},{usersum},{comp},{compsum}")
while usersum < 21 and compsum < 21:

    print(f"User cards: {user}")
    print(f"Comp card: {comp[0]}")

    ask=input("Do you want to get another card?  (y/n): ")

    if ask == "y":
        dealcard()
        print(user)
        usersum+=user[2]
        if usersum>21:
            print("You lose")
        elif compsum<17:
            compsum+=comp[2]
        elif usersum>compsum:
            print("You win")
        elif compsum>usersum:
            print("You lose")
        else:
            print("Draw")
    elif ask == "n":
        if usersum>compsum:
            print("You win")
        elif compsum>usersum:
            print("You lose")
        else:
            print("Draw")

if compsum==21 and usersum!=21:
    print(f"{compsum}, {usersum}")
    print("You lose")
elif usersum==21:
    print(f"{compsum}, {usersum}")
    print("You win")
        

