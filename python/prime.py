n=int(input("Enter the number: "))
prime=[]
f=1
for i in range(2,n+1):
    if n%i==0:
        f=0
        break

if f==0:
    print(n," is not prime")
else:
    print(n," is prime")