n=int(input("Enter number of years: "))
c=int(input("Enter capital amount: "))
p=int(input("Enter the interest rate per year: "))
sum=c
for i in range (0,n):
    sum=sum+p*c/100

print(sum)