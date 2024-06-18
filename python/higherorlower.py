

resources={
    "water": 250,
    "milk": 200,
    "coffee": 100
}

menu={
    "espresso": {
        "ingredients": {
            "water":50,
            "milk": 0,
            "coffee": 18
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    }
}



option=input("What would you like? (espresso/latte): ").lower()

coin=int(input("Please insert coin"))

def balancecheck():
    if option=="espresso":
        if resources["water"]>=50 and resources["coffee"]>=18:
            if coin>=1.5:
                resources["water"]-=50
                resources["coffee"]-=18
                print("Here is your espresso. Enjoy!!")
                print(f"Here is your change {coin-1.5}")
            else:
                print("Not enough coins")
        else:
            print("Not enough resources")
    if option=="latte":
        if resources["water"]>=200 and resources["coffee"]>=24 and resources["milk"]>=150:
            if coin>=2.5:
                resources["water"]-=200
                resources["coffee"]-=24
                resources["milk"]-=150
                print("Here is your espresso. Enjoy!!")
                print(f"Here is your change {coin-2.5}")
            else:
                print("Not enough coins")
        else:
            print("Not enough resources")
    if option=="report":
        print(resources)

print(resources)
               

balancecheck()
print(resources)
