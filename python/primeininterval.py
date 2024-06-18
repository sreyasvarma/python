n=int(input("Enter the number: "))
prime=[]
f=1
for p in range(2,n):
    for i in range(2,n):
        if p%i==0:
            f=0
            break
    if f==1:
        prime.append(p)
    else:
        continue        
            