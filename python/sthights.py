stheights=input("ENter the heights followed by space").split()
n=0
stheights=[int(i) for i in stheights]
print(stheights)
sum=0
for i in stheights:
    sum+=i
    n=n+1
av=sum/n
print(av)