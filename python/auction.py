
data={}

maxbid=0
shouldcontinue="yes"

while shouldcontinue=="yes":
    name=input("Enter the name")
    bid=int(input("Enter the bid"))
    if bid>maxbid:
        maxbid=bid
        winner=name
        
    data[name]=bid
    shouldcontinue=input("Do you want to continue?")

print(f"maximum bid is {maxbid}, winner is {winner}")  




