n=int(input("Enter the number: "))
sum=0
arm=n
while n%10!=0:
    i=n%10
    sum+=i**3
    n//=10

if sum==arm:
    print("$n is armstrong number")
else:
    print("$n is not armstrong number")