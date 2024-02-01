#simple interest

p=int(input("Enter the principal amount: "))
i=int(input("Enter the interest rate: "))

y=int(input("Enter number of years: "))

interest=(p*i/100)
totalinterest=y*interest
totalamount=p+totalinterest

print("Interest per year: ", interest)
print("Total interest: ", totalinterest)
print("Total amount: ", totalamount)
