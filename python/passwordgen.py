import random
letters=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbols=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]
numbers=["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
password=[]
lettersno = int(input("How many letters? "))
symbolsno = int(input("How many symbols? "))
numbersno = int(input("How many numbers? "))
for i in range(1,lettersno+1):
    password += random.choice(letters)

for i in range(1,symbolsno+1):
    password += random.choice(symbols)

for i in range(1,numbersno+1):
    password += random.choice(numbers)

random.shuffle(password)
passw=""
for i in password:
    passw+=i

print(passw)
