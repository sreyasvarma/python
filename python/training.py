# import random

# names=input("Who all are here? ")
# names=names.split(", ")
# print(names)
# n=len(names)
# payee=random.randint(0,n)
# print(f"The lucky person is {names[payee]} ! ")
row1=['O','O','O']
row2=['O','O','O']
row3=['O','O','O']
map=[row1]+[row2]+[row3]
n=int(input("Enter the number"))
m=n%10
n=n//10
map[n][m]='X'
print(f"{row1}\n{row2}\n{row3}")