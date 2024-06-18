n=int(input("Enter value of n:"))

fac=1
for i in range(1,n):
    fac=fac*i
    i+=1

print(fac)