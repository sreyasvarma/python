sum=0
n=int(input("enter the number of nums"))
for i in range(0,n):
    a=int(input("Enter a number: "))
    sum=sum+a

average=sum/n
print("Average of ",n,"numbers is ", average)
