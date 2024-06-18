l=[]
n=int(input("Enter the numbr of elements: "))
for i in range(0,n):
    i=input("Enter a element in list :")
    l.append(i)

last=l[n-1]
first=l[0]
l[n-1]=first
l[0]=last

print(l)
